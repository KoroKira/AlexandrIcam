#include <stdio.h>
#include <ctype.h>

int main() {
    char texte[1000];
    int occurrences[26] = {0}; 

    printf("Entrez un texte : \n");
    fgets(texte, sizeof(texte), stdin);

    for (int i = 0; texte[i] != '\0'; i++) {
        char caractere = tolower(texte[i]);
        if (isalpha(caractere)) {
            occurrences[caractere - 'a']++;
        }
    }
    
    printf("Occurrences des lettres :\n");
    for (int i = 0; i < 26; i++) {
        if (occurrences[i] > 0) {
            char lettre = 'a' + i;
            printf("%c=%d, ", lettre, occurrences[i]);
        }
    }

    return 0;
}
