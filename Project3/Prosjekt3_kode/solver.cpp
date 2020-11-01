#include "solver.hpp"
#include "planet.hpp"
#include <iostream>
#include <cmath>
#include "time.h"

// Initialiserer og legger til objekter:
//---------------------------------------

solver::solver(double radi)
{                      // Definerer globale variabler:
    total_planets = 0; // Her legger vi til antall planeter.
    radius = radi;
    total_mass = 0;      // Her legger vil til den totale massen.
    G = 4 * M_PI * M_PI; // Gravitasjonskonstanten.
    totalKinetic = 0;    // Her lagres den totale kinetiske energien.
    totalPotential = 0;  // Her lagres den totale potensielle energien.
}

void solver::add(planet newplanet)
{                                     // Legger til planeter.
    total_planets += 1;               // Legger til det totale antallet objekter.
    total_mass += newplanet.mass;     // Legger til den totale massen.
    all_planets.push_back(newplanet); // Legger objektet til systemet av objekter.
}

// Regner ut gravitasjonskraft og setter opp matrise for å lagre akselerasjonsverdier:
//------------------------------------------------------------------------------------

void solver::GravitationalForce(planet &current, planet &other,
                                double &Fx, double &Fy, double &Fz, double epsilon, double beta, int GR)
{                                                                       // Funksjon som regner ut gravitasjonskraften mellom to objekter.
    double relative_velocity[3];
    double rel_cor;
    double c = 63197.8;
    double relative_distance[3];                                        // Den relative avstanden mellom nåverende objekt og alle andre planeter.
    for (int j = 0; j < 3; j++)                                         // Finner retningsvektoren i tre dimensjoner.
        relative_distance[j] = current.position[j] - other.position[j]; // Dette er vektoren (med retning)
    double r = current.distance(other);
    double l_x = current.position[1] * current.velocity[2] - current.position[2] * current.velocity[1];
    double l_y = current.position[0] * current.velocity[2] - current.position[2] * current.velocity[0];
    double l_z = current.position[0] * current.velocity[1] - current.position[1] * current.velocity[0];
    double l = sqrt(l_x * l_x + l_y * l_y + l_z * l_z); // Lengden av vektoren.
    double smoothing = epsilon * epsilon * epsilon;

    if (GR == 0)
    {
        rel_cor = 1.0 + (3.0 * l * l) / (r * r * c * c);
    }
    else if (GR == 1)
    {
        rel_cor = 1.0;
    }
    // Regner ut krefter i alle retninger.
    Fx -= (this->G * current.mass * other.mass * relative_distance[0] / (pow(r, beta) + smoothing))* rel_cor;
    Fy -= (this->G * current.mass * other.mass * relative_distance[1] / (pow(r, beta) + smoothing))* rel_cor;
    Fz -= (this->G * current.mass * other.mass * relative_distance[2] / (pow(r, beta) + smoothing))* rel_cor;
}

double **solver::setup_matrix(int height, int width)
{ // Setter opp en matrise som skal brukes til å lagre akselerasjonsverdier.
    double **matrix;
    matrix = new double *[height];
    for (int i = 0; i < height; i++)
        matrix[i] = new double[width];
    // Setter alle verdier i matrisen til null:
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            matrix[i][j] = 0.0;
        }
    }
    return matrix;
}

void solver::delete_matrix(double **matrix)
{ // Funksjon som fjerner minne for akselerasjonsmatrisen.
    for (int i = 0; i < total_planets; i++)
        delete[] matrix[i];
    delete[] matrix;
}

// Finner antall planeter som er bundet og energien i systemet:
//--------------------------------------------------------------

bool solver::Bound(planet OnePlanet)
{ // Dette er en betingelse som bestemmer om et objekt har forlatt systemet.
    return ((OnePlanet.kinetic + OnePlanet.potential) < 0.0);
}

void solver::KineticEnergySystem()
{ // Regner ut den totale kinetiske energien fra funksjon i planet.hpp.
    totalKinetic = 0;
    for (int nr = 0; nr < total_planets; nr++)
    {
        planet &Current = all_planets[nr];
        Current.kinetic = Current.KineticEnergy();
    }
}

void solver::PotentialEnergySystem(double epsilon)
{ // Regner ut den totale potensielle energien fra funksjon i planet.hpp.
    totalPotential = 0;
    for (int nr = 0; nr < total_planets; nr++)
    {
        planet &Current = all_planets[nr];
        Current.potential = 0;
    }
    for (int nr1 = 0; nr1 < total_planets; nr1++)
    {
        planet &Current = all_planets[nr1];
        for (int nr2 = nr1 + 1; nr2 < total_planets; nr2++)
        {
            planet &Other = all_planets[nr2];
            Current.potential += Current.PotentialEnergy(Other, G, epsilon);
            Other.potential += Other.PotentialEnergy(Current, G, epsilon);
        }
    }
}

double solver::EnergyLoss()
{               // Regner ut energitapet.
    bool bound; // Denne er True eller False og hentes fra bound() funksjonen.
    vector<int> indices;
    double EnergyLoss = 0;
    for (int nr = 0; nr < total_planets; nr++)
    {
        planet &Current = all_planets[nr];
        bound = this->Bound(Current);
        if (!bound) // Hvis True:
        {
            indices.push_back(nr); // Legger til element i enden av vektor.
        }
    }
    for (int i = 0; i < indices.size(); i++) // Legger til energien fra planeter som forlater systemet:
        EnergyLoss += all_planets[indices[i]].KineticEnergy();
    return EnergyLoss; // Retunerer energitapet som skyldes "unbound" planeter.
}

// Numeriske løsningsmetoder:
//---------------------------

void solver::Euler(int dimension, int integration_points, double final_time,
                   int print_number, double epsilon, double beta, int GR)
{                                                                 // Euler metoden.
    double time_step = final_time / ((double)integration_points); // Definerer tidssteg.
    double time = 0.0;                                            // Her lagrer vi den totale tiden.
    double loss = 0.;                                             // Her lagrer vi potensielt energitap.
    int lostPlanets;
    // Lager fil for datalagring:
    char *filename_EU = new char[1000];
    char *filenameE_EU = new char[1000];
    char *filenameB_EU = new char[1000];
    char *filenameLost_EU = new char[1000];
    sprintf(filename_EU, "Textfiles/PlanetsEU_%d.txt", total_planets);
    sprintf(filenameE_EU, "Textfiles/PlanetsEU_energy_%d.txt", total_planets);
    sprintf(filenameB_EU, "Textfiles/Planetsbound_%d.txt", total_planets);
    sprintf(filenameLost_EU, "Textfiles/Planetslost_%d.txt", total_planets);
    std::ofstream output_file(filename_EU);
    std::ofstream output_energy(filenameE_EU);
    std::ofstream output_bound(filenameB_EU);
    std::ofstream output_lost(filenameLost_EU);
    // Kaller på matrisfunksjonen som gir oss matrise der vi lagrer akselerasjonsverdier;
    double **acceleration = setup_matrix(total_planets, 3);
    double Fx, Fy, Fz; // Her lagres kreftene i hver dimensjon.
    // Skriver initialverdiene til fil:
    print_position(output_file, dimension, time, print_number); // Skriver posisjon til fil.
    print_energy(output_energy, time, epsilon);                 // Skriver energi til fil.
    int n = 0;                                                  // Indeks for å finne tapte planeter.
    lostPlanets = 0;
    output_lost << time << "\t" << lostPlanets << std::endl;
    n += 1;
    clock_t planet_EU, finish_EU;
    planet_EU = clock(); // Tar tid på metode.
    time += time_step;   // Legger tidssteg til den totale tiden.
    while (time < final_time)
    {
        lostPlanets = 0;
        // Looper ovver alle planetene:
        for (int nr1 = 0; nr1 < total_planets; nr1++)
        {
            planet &current = all_planets[nr1]; // Nåverende planet.
            // Regner ut ny posisjon for nåverende planet:
            for (int j = 0; j < dimension; j++)
            {
                current.position[j] += current.velocity[j] * time_step;
            }
            Fx = Fy = Fz = 0.0; // Nullstiller krefter.
            // Regner ut krefter i hver dimensjon:
            for (int nr2 = nr1 + 1; nr2 < total_planets; nr2++)
            { // Looper gjennom planeter med større indeks enn den vi ser på.
                planet &other = all_planets[nr2];
                GravitationalForce(current, other, Fx, Fy, Fz, epsilon, beta, GR);
            }
            // Akselerasjon for nåverende planet:
            acceleration[nr1][0] = Fx / current.mass;
            acceleration[nr1][1] = Fy / current.mass;
            acceleration[nr1][2] = Fz / current.mass;

            // Ny hastighet for nåverende planet:
            for (int j = 0; j < dimension; j++)
                current.velocity[j] += time_step * acceleration[nr1][j];
        }
        // Skriver verdiene til fil:
        print_position(output_file, dimension, time, print_number);
        print_energy(output_energy, time, epsilon);
        loss += EnergyLoss(); // Legger til energitap.

        for (int nr = 0; nr < total_planets; nr++)
        { // Finner antall tapte planeter:
            planet &Current = all_planets[nr];
            if (!(this->Bound(Current)))
            {
                lostPlanets += 1;
            }
        }
        output_lost << time << "\t" << lostPlanets << std::endl;
        n += 1;
        time += time_step;
    }
    // Stopper tidtaking og skriver ut verdier:
    finish_EU = clock();
    std::cout << "Total time = "
              << "\t" << ((float)(finish_EU - planet_EU) / CLOCKS_PER_SEC)
              << " seconds" << std::endl;
    std::cout << "One time step = "
              << "\t" << ((float)(finish_EU - planet_EU) / CLOCKS_PER_SEC) / integration_points << " seconds" << std::endl;
    std::cout << "Total energyloss due to unbound planets: "
              << loss << std::endl;

    double boundPlanets = 0;
    for (int nr = 0; nr < total_planets; nr++)
    {
        planet &Current = all_planets[nr];
        if (this->Bound(Current))
        {
            output_bound << nr << std::endl;
            boundPlanets += 1;
        }
    }
    std::cout << "There are " << boundPlanets
              << " bound planets at the end of the run" << std::endl;

    // Lukker filer:
    output_file.close();
    output_energy.close();
    output_bound.close();
    output_lost.close();

    // Tømmer minne for matrien:
    delete_matrix(acceleration);
}

void solver::VelocityVerlet(int dimension, int integration_points,
                            double final_time, int print_number, double epsilon, double beta, int GR)
{                                                                 // Velocity Verlet metoden.
    double time_step = final_time / ((double)integration_points); // Definerer tidssteg.
    double time = 0.0;                                            // Her lagrer vi den totale tiden.
    double loss = 0.;                                             // Her lagrer vi potensielt energitap.
    int lostPlanets;
    // Lager file for datalagring:
    char *filename = new char[1000];
    char *filenameE = new char[1000];
    char *filenameB = new char[1000];
    char *filenameLost = new char[1000];
    sprintf(filename, "Textfiles/PlanetsVV_%d.txt", total_planets);
    sprintf(filenameE, "Textfiles/PlanetsVV_energy_%d.txt", total_planets);
    sprintf(filenameB, "Textfiles/Planetsbound_%d.txt", total_planets);
    sprintf(filenameLost, "Textfiles/Planetslost_%d.txt", total_planets);
    std::ofstream output_file(filename);
    std::ofstream output_energy(filenameE);
    std::ofstream output_bound(filenameB);
    std::ofstream output_lost(filenameLost);
    // Kaller på matrisfunksjonen som gir oss matrise der vi lagrer akselerasjonsverdier.
    double **acceleration = setup_matrix(total_planets, 3);
    double **acceleration_new = setup_matrix(total_planets, 3);
    double Fx, Fy, Fz, Fxnew, Fynew, Fznew; // Her lagres kreftene i hver dimensjon.
    // Skriver initialverdiene til fil:
    print_position(output_file, dimension, time, print_number); // Skriver posisjon til fil.
    print_energy(output_energy, time, epsilon);                 // Skriver energi til fil.
    int n = 0;                                                  // Indeks for tapte planeter.
    lostPlanets = 0;                                         // Tapte planeter legges til her.
    output_lost << time << "\t" << lostPlanets << std::endl;
    n += 1;                       // Neste planet.
    clock_t planet_VV, finish_VV; // Tar tid på metode.
    planet_VV = clock();
    time += time_step;
    while (time < final_time)
    {
        lostPlanets = 0;
        // Looper over alle planeter.
        for (int nr1 = 0; nr1 < total_planets; nr1++)
        {
            planet &current = all_planets[nr1];         // Nåverende planet.
            Fx = Fy = Fz = Fxnew = Fynew = Fznew = 0.0; // Nullstiller krefter.
            // Regner ut krefter i hver dimensjon:
            // Calculate forces in each dimension
            for (int nr2 = 0; nr2 < total_planets; nr2++)
            {
                if (nr2 != nr1)
                {
                    planet &other = all_planets[nr2];
                    GravitationalForce(current, other, Fx, Fy, Fz, epsilon, beta, GR);
                }
            }

            // Akselerasjon for nåverende planet i hver dimensjon.
            acceleration[nr1][0] = Fx / current.mass;
            acceleration[nr1][1] = Fy / current.mass;
            acceleration[nr1][2] = Fz / current.mass;

            // Regner ut ny posisjon.
            for (int j = 0; j < dimension; j++)
            {
                current.position[j] += current.velocity[j] * time_step + 0.5 * time_step * time_step * acceleration[nr1][j];
            }

            // Loop over all other planets
            for (int nr2 = 0; nr2 < total_planets; nr2++)
            {
                if (nr2 != nr1)
                {
                    planet &other = all_planets[nr2];
                    GravitationalForce(current, other, Fxnew, Fynew, Fznew, epsilon, beta, GR);
                }
            }

            // Den nye akslerasjonen.
            acceleration_new[nr1][0] = Fxnew / current.mass;
            acceleration_new[nr1][1] = Fynew / current.mass;
            acceleration_new[nr1][2] = Fznew / current.mass;
            // Regner ut den nye hastigheten:
            for (int j = 0; j < dimension; j++)
                current.velocity[j] += 0.5 * time_step * (acceleration[nr1][j] + acceleration_new[nr1][j]);
        }
        // Skriver verdier til fil:
        if (integration_points > 10000000)
        {
            if (time > final_time - 2 * time_step)
            {
                std::cout << "Too many intergration points to print every time step" << std::endl;
                std::cout << "Only printing last values to file"
                          << " " << final_time << " " << time << std::endl;
                print_position(output_file, dimension, time, print_number);
                print_energy(output_energy, time, epsilon);
            }
        }
        else
        {
            print_position(output_file, dimension, time, print_number);
            print_energy(output_energy, time, epsilon);
        }
        loss += EnergyLoss(); // Legger til evt. tapt energi.
        for (int nr = 0; nr < total_planets; nr++)
        { // Finner antall tapte planeter:
            planet &Current = all_planets[nr];
            if (!(this->Bound(Current)))
            {
                lostPlanets += 1;
            }
        }
        output_lost << time << "\t" << lostPlanets << std::endl;
        n += 1;
        time += time_step;
    }
    // Stopper tidtaking og skriver ut verdier:
    finish_VV = clock();
    std::cout << "Total time = "
              << "\t" << ((float)(finish_VV - planet_VV) / CLOCKS_PER_SEC)
              << " seconds" << std::endl;
    std::cout << "One time step = "
              << "\t" << ((float)(finish_VV - planet_VV) / CLOCKS_PER_SEC) / integration_points << " seconds" << std::endl;
    std::cout << "Total energyloss due to unbound planets: "
              << loss << std::endl;

    double boundPlanets = 0;
    for (int nr = 0; nr < total_planets; nr++)
    {
        planet &Current = all_planets[nr];
        if (this->Bound(Current))
        {
            output_bound << nr << std::endl;
            boundPlanets += 1;
        }
    }
    std::cout << "There are " << boundPlanets
              << " bound planets at the end of the run" << std::endl;
    // Lukker filer:
    output_file.close();
    output_energy.close();
    output_bound.close();
    output_lost.close();

    // Tømmer minne for matriene:
    delete_matrix(acceleration);
    delete_matrix(acceleration_new);
}

// Her skriver vi til filer:
//--------------------------

void solver::print_position(std::ofstream &output, int dimension, double time,
                            int number)
{ // Skriver masse, posisjon og hastighet til fil. Denne blir kalt på i hvert tidssteg.
    if (dimension > 3 || dimension <= 0)
        dimension = 3; // Setter dimensjonen til 3.
    else
    {
        for (int i = 0; i < number; i++)
        { // Vi skriver informasjonen for hver planet:
            planet &current = all_planets[i];
            output << time << "\t" << i + 1 << "\t" << current.mass;
            for (int j = 0; j < dimension; j++)
                output << "\t" << current.position[j];
            for (int j = 0; j < dimension; j++)
                output << "\t" << current.velocity[j];
            output << std::endl;
        }
    }
}

void solver::print_energy(std::ofstream &output, double time, double epsilon)
{ // Skriver energien til fil. Denne blir kalt på i hvert tidssteg.

    this->KineticEnergySystem();
    this->PotentialEnergySystem(epsilon);
    for (int nr = 0; nr < total_planets; nr++)
    { // Vi skriver energien for hver planet:
        planet &Current = all_planets[nr];
        output << time << "\t" << nr << "\t";
        output << Current.kinetic << "\t" << Current.potential << std::endl;
    }
}