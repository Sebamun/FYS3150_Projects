#include "prosjekt2.hpp"

int main(int argc, char const *argv[]) {
    string filename = argv[1];
    mat U;
    Initialize(5, 0, 1, U);
    check(5, 1, U, filename);
    return 0;
}
