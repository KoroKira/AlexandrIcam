#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

class Matrice {
private:
    int m_Nlig;
    int m_Ncol;
    double** m_Tab;

public:
    Matrice() : m_Nlig(0), m_Ncol(0), m_Tab(nullptr) {}

    Matrice(int a_l, int a_c) : m_Nlig(a_l), m_Ncol(a_c) {
        m_Tab = new double*[m_Nlig];
        for (int i = 0; i < m_Nlig; ++i) {
            m_Tab[i] = new double[m_Ncol];
        }
    }

    // Constructeur de recopie
    Matrice(const Matrice& other) : m_Nlig(other.m_Nlig), m_Ncol(other.m_Ncol) {
        m_Tab = new double*[m_Nlig];
        for (int i = 0; i < m_Nlig; ++i) {
            m_Tab[i] = new double[m_Ncol];
            for (int j = 0; j < m_Ncol; ++j) {
                m_Tab[i][j] = other.m_Tab[i][j];
            }
        }
    }

    // Constructeur à partir d'un fichier
    explicit Matrice(const std::string& fileName) {
        std::ifstream file(fileName);
        if (file.is_open()) {
            file >> m_Nlig >> m_Ncol;
            m_Tab = new double*[m_Nlig];
            for (int i = 0; i < m_Nlig; ++i) {
                m_Tab[i] = new double[m_Ncol];
                for (int j = 0; j < m_Ncol; ++j) {
                    file >> m_Tab[i][j];
                }
            }
            file.close();
        } else {
            std::cerr << "Erreur lors de l'ouverture du fichier." << std::endl;
        }
    }

    ~Matrice() {
        for (int i = 0; i < m_Nlig; ++i) {
            delete[] m_Tab[i];
        }
        delete[] m_Tab;
    }

    int get_Nlig() const { return m_Nlig; }
    int get_Ncol() const { return m_Ncol; }

    void set_Nlig(int l) { m_Nlig = l; }
    void set_Ncol(int c) { m_Ncol = c; }

    void SaisieAll() {
        for (int i = 0; i < m_Nlig; ++i) {
            for (int j = 0; j < m_Ncol; ++j) {
                std::cout << "Entrer l'élément (" << i + 1 << ", " << j + 1 << ") : ";
                std::cin >> m_Tab[i][j];
            }
        }
    }

    void Affiche() const {
        for (int i = 0; i < m_Nlig; ++i) {
            for (int j = 0; j < m_Ncol; ++j) {
                std::cout << std::setw(8) << m_Tab[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    double trace() const {
        double result = 0.0;
        for (int i = 0; i < std::min(m_Nlig, m_Ncol); ++i) {
            result += m_Tab[i][i];
        }
        return result;
    }

    double operator()(int a_l, int a_c) const {
        return m_Tab[a_l][a_c];
    }

    Matrice operator*(const Matrice& other) const {
        Matrice result(m_Nlig, other.m_Ncol);
        for (int i = 0; i < m_Nlig; ++i) {
            for (int j = 0; j < other.m_Ncol; ++j) {
                result.m_Tab[i][j] = 0.0;
                for (int k = 0; k < m_Ncol; ++k) {
                    result.m_Tab[i][j] += m_Tab[i][k] * other.m_Tab[k][j];
                }
            }
        }
        return result;
    }

    // Surcharge des opérateurs +, -, et =
    Matrice operator+(const Matrice& other) const {
        Matrice result(m_Nlig, m_Ncol);
        for (int i = 0; i < m_Nlig; ++i) {
            for (int j = 0; j < m_Ncol; ++j) {
                result.m_Tab[i][j] = m_Tab[i][j] + other.m_Tab[i][j];
            }
        }
        return result;
    }

    Matrice operator-(const Matrice& other) const {
        Matrice result(m_Nlig, m_Ncol);
        for (int i = 0; i < m_Nlig; ++i) {
            for (int j = 0; j < m_Ncol; ++j) {
                result.m_Tab[i][j] = m_Tab[i][j] - other.m_Tab[i][j];
            }
        }
        return result;
    }

    void setV(int a_l, int a_c, double a_Val) {
        m_Tab[a_l][a_c] = a_Val;
    }

    void re_size(int a_lig, int a_col) {
        // Cette fonction devrait être implémentée en fonction de votre besoin
        // par exemple, en créant une nouvelle matrice avec les nouvelles dimensions
        // et en copiant les valeurs de l'ancienne matrice dans la nouvelle.
    }

    // Fonction init pour remplir toute la matrice avec une constante
    void init(double value) {
        for (int i = 0; i < m_Nlig; ++i) {
            for (int j = 0; j < m_Ncol; ++j) {
                m_Tab[i][j] = value;
            }
        }
    }
};

int main() {
    // Exemple d'utilisation
    Matrice M1("matrice1.txt");
    Matrice M2("matrice2.txt");

    std::cout << "Matrice M1 :" << std::endl;
    M1.Affiche();

    std::cout << "Matrice M2 :" << std::endl;
    M2.Affiche();

    // Transpose M1
    Matrice M1_transpose = M1;  // Utilisation du constructeur de recopie
    M1_transpose.re_size(M1.get_Ncol(), M1.get_Nlig);

    for (int i = 0; i < M1.get_Nlig(); ++i) {
        for (int j = 0; j < M1.get_Ncol(); ++j) {
            M1_transpose.setV(j, i, M1(i, j));
        }
    }

    std::cout << "Transpose de M1 :" << std::endl;
    M1_transpose.Affiche();

    // Multiplication M1 par M2
    Matrice result_mult = M1 * M2;

    std::cout << "Multiplication de M1 par M2 :" << std::endl;
    result_mult.Affiche();

    return 0;
}
