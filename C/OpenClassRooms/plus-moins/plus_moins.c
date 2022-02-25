#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int MAX = 100, MIN = 1, nombreMystere = 0, J = 0, difficulty = 0, number = 0, n = 0;

    while (J != 1 && J != 2){
        printf("=== Menu ===\n");
        printf("1. 1 Joueur\n");
        printf("2. 2 Joueurs \n\n");
        printf("Que choisisez-vous ?\n");
        scanf("%d", &J);
        system("cls");
    }

    if (J == 1){
        while (difficulty != 1 && difficulty != 2 && difficulty != 3){
            printf("=== Difficulty ===\n");
            printf("1. easy\n");
            printf("2. normal\n");
            printf("3. hard\n\n");
            printf("Que choisisez-vous ?\n");
            scanf("%d", &difficulty);
            system("cls");
        }

        switch (difficulty){
        case 1:
            break;
        case 2:
            MAX = 1000;
            break;
        case 3:
            MAX = 10000;
        }

        srand(time(NULL));
        nombreMystere = (rand() % (MAX - MIN + 1)) + MIN;
    }else {
        printf("Joueur 1, choisisez un nombre :\n");
        scanf("%d", &nombreMystere);
        system("cls");
    }

    printf("Quel est le nombre ?\n");
    scanf("%d", &number);

    while (number != nombreMystere){
        if (number > nombreMystere){
            printf("C'est moins !\n");
            printf("\nQuel est le nombre ?\n");
            scanf("%d", &number);
            n++;
        }else if (number < nombreMystere){
            printf("C'est plus !\n");
            printf("\nQuel est le nombre ?\n");
            scanf("%d", &number);
            n++;
        }
    }
    printf("\nBravo, vous avez trouve le nombre mystere en %d coup(s).\n", n+1);
    return 0;
}
