// Différents types d'erreur
typedef enum {
    AUTRES_ERREURS
} erreur_t;

// Différents types de lexèmes existants
typedef enum {
    REEL, OPERATEUR, FONCTION, INCONNU, FIN, PARENTHESE_OUV, PARENTHESE_FERM, VARIABLE
} lexem_t;

// Différents types d'opérateurs existants
typedef enum {
    ADDITION, SOUSTRACTION, MULTIPLICATION, DIVISION, PUISSANCE
} operateur_t;

// Différents types de fonctions existantes
typedef enum {
    ABS, SIN, SQRT, LOG, COS, TAN, EXP, VALEUR_NEGATIVE
} fonction_t;

// Union des valeurs pour chaque type
typedef union {
    float reel;
    fonction_t fonction;
    operateur_t operateur;
} valeur_t;

// Jeton (l'objet qui contient le lexem et sa valeur)
typedef struct {
    lexem_t lexeme;
    valeur_t valeur;
} jeton_t;


// Declaration de l'arbre (avec des pointeurs vers les jetons)
typedef struct Node {
    jeton_t jeton;
    struct Node *pjeton_precedent;
    struct Node *pjeton_suivant;
} Node;
typedef Node *Arbre;