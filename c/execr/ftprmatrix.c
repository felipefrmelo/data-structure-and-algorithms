
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

// criar um estrutura para descrever restaurantes( nome, preco_medio, endreço, tipo)
// criar um lista ligada que apresente restaurantes por tipo e que são indexados pelo preço
// o menor deve ser o primeiro da lista
// escreva um programa que peça o tipo de comida para o usuario e imprima os restaurantes
//que oferecem ees tipo

typedef enum Tipo
{
    JAPA,
    BRASILEIRA,
    LANCHES,
    PIZZA
} Tipo;

typedef struct Restaurante
{
    char nome[30];
    int precoMedio;
    char endereco[50];
    Tipo tipo;

} Restaurante;

typedef struct Node
{
    Restaurante restaurante;
    struct Node *next;

} Node;

Node *lista;

void adicionaRestauranteTipoPizza(Restaurante *restaurante)
{
    Node *ultimo = malloc(sizeof(Node));
    Node *atual = malloc(sizeof(Node));

    ultimo->restaurante = *restaurante;
    if (lista == NULL)
    {
        lista = ultimo;
        return;
    }

    atual = lista;
    while (atual->next != NULL)
    {
        atual = atual->next;
    }
    atual->next = ultimo;
}

void imprimeRestaurantes()
{

    if (lista == NULL)
    {
        printf("Lista vazia\n");
        return;
    }

    Node *atual = malloc(sizeof(Node));
    atual = lista;
    do
    {
        printf("\nNome: %s\n", atual->restaurante.nome);
        printf("Preco medio: %d\n", atual->restaurante.precoMedio);
        printf("Tipo: %d\n", atual->restaurante.tipo);
        printf("Endereço: %s\n\n", atual->restaurante.endereco);
        atual = atual->next;

    } while (atual);
}

Restaurante *criaRestaurante(char nome[30], int precoMedio, char endereco[50], Tipo tipo)
{
    Restaurante *result = malloc(sizeof(Restaurante));
    ;
    strcpy(result->nome, nome);
    result->precoMedio = precoMedio;
    strcpy(result->endereco, endereco);
    result->tipo = tipo;
    return result;
}

int getTipo()
{

    int tipo;
    printf("Escolha o tipo:\n");
    printf("Japa: %d\n", JAPA);
    printf("Brasileira : %d\n", BRASILEIRA);
    printf("Lanches: %d\n", LANCHES);
    printf("Pizza: %d\n", PIZZA);

    scanf("%d", &tipo);

    switch (tipo)
    {
    case JAPA:
        return JAPA;
    case BRASILEIRA:
        return BRASILEIRA;
    case PIZZA:
        return PIZZA;
    case LANCHES:
        return LANCHES;
    default:
        break;
    }
}
int main(int argc, char const *argv[])
{
    Restaurante *pizzaria1 = criaRestaurante("Pizza a", 100, "Rua virgilio polo", PIZZA);
    Restaurante *pizzaria2 = criaRestaurante("Pizza b", 200, "Rua Teste", PIZZA);
    Restaurante *lanchonete = criaRestaurante("Lanche b", 22, "Rua lanche", LANCHES);

    // imprimeRestaurantes();

    char opcao, nome[30], endereco[30];
    int preco, tipo;

    while (opcao != 'n')
    {
        printf("\nDigite o nome: ");
        scanf("%s", nome);
        printf("Digite o preco: ");
        scanf("%d", &preco);
        printf("Digite o endereco: ");
        scanf("%s", endereco);
        tipo = getTipo();
        adicionaRestauranteTipoPizza(criaRestaurante(nome, preco, endereco, tipo));

        printf("\n\nDeseja continuar ? (s/n) ");
        scanf("%s", &opcao);
    }

    adicionaRestauranteTipoPizza(pizzaria1);
    adicionaRestauranteTipoPizza(pizzaria2);
    adicionaRestauranteTipoPizza(lanchonete);
    imprimeRestaurantes();
    return 0;
}
