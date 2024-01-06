<!-- omit in toc -->
# Contribuer à Cours-CommunistIcam

Cette description est totalement stolen d'une docu et traduite en anglais mdr, j'ai la flemme de checker mais tranquille
Tout d'abord, merci de prendre le temps de contribuer ! ❤️

Tous types de contributions sont encouragés et appréciés. Consultez la [Table des matières](#table-of-contents) pour connaître les différentes façons d'aider et les détails sur la manière dont ce projet les gère. Veuillez vous assurer de lire la section pertinente avant de faire votre contribution. Cela facilitera beaucoup la tâche pour nous, les mainteneurs, et rendra l'expérience plus fluide pour tous les intervenants. La communauté attend avec impatience vos contributions. 🎉

> Et si vous aimez le projet mais n'avez tout simplement pas le temps de contribuer, c'est bien. Il existe d'autres moyens faciles de soutenir le projet et de montrer votre appréciation, que nous apprécierions également :
> - Mettez une étoile sur le projet
> - Tweetez à ce sujet
> - Faites référence à ce projet dans le readme de votre projet
> - Mentionnez le projet lors de rencontres locales et parlez-en à vos amis/collègues

<!-- omit in toc -->
## Table des matières

- [Code de conduite](#code-de-conduite)
- [J'ai une question](#jai-une-question)
- [Je veux contribuer](#je-veux-contribuer)
- [Signalement de bogues](#signalement-de-bogues)
- [Suggérer des améliorations](#suggérer-des-améliorations)
- [Votre première contribution de code](#votre-première-contribution-de-code)
- [Améliorer la documentation](#améliorer-la-documentation)
- [Guides de style](#guides-de-style)
- [Messages de commit](#messages-de-commit)
- [Rejoindre l'équipe du projet](#rejoindre-léquipe-du-projet)


## Code de conduite

Ce projet et toutes les personnes qui y participent sont régis par le [Code de conduite de Cours-CommunistIcam](https://github.com/KoroKira/Cours-CommunistIcam/blob/main/CODE_OF_CONDUCT.md). En participant, vous vous engagez à respecter ce code. Veuillez signaler tout comportement inacceptable à <>.

## J'ai une question

> Si vous avez une question, nous partons du principe que vous avez lu la [Documentation](https://github.com/KoroKira/Cours-CommunistIcam/blob/main/documentation.md) disponible.

Avant de poser une question, il est préférable de rechercher des [Issues](https://github.com/KoroKira/Cours-CommunistIcam/issues) existantes qui pourraient vous aider. Si vous trouvez une issue appropriée et avez encore besoin de clarification, vous pouvez écrire votre question dans cette issue. Il est également conseillé de rechercher des réponses sur Internet en premier.

Si vous avez toujours besoin de poser une question et d'obtenir des éclaircissements, nous vous recommandons ce qui suit :

- Ouvrez une [Issue](https://github.com/KoroKira/Cours-CommunistIcam/issues/new).
- Fournissez autant de contexte que possible sur ce que vous rencontrez.
- Fournissez les versions du projet et de la plateforme (nodejs, npm, etc.), selon ce qui semble pertinent.

Nous nous occuperons ensuite de l'issue dès que possible.

<!--
Vous voudrez peut-être créer un tag d'issue distinct pour les questions et l'inclure dans cette description. Les gens devraient alors taguer leurs issues en conséquence.

En fonction de la taille du projet, vous voudrez peut-être externaliser les questions, par exemple sur Stack Overflow ou Gitter. Vous pouvez ajouter des moyens de contact et d'information supplémentaires :
- IRC
- Slack
- Gitter
- Tag Stack Overflow
- Blog
- FAQ
- Roadmap
- Liste de diffusion par e-mail
- Forum
-->

## Je veux contribuer

> ### Avis légal <!-- omit in toc -->
> Lorsque vous contribuez à ce projet, vous devez accepter que vous avez rédigé 100% du contenu, que vous avez les droits nécessaires sur le contenu et que le contenu que vous contribuez peut être fourni sous la licence du projet.

### Signalement de bogues

<!-- omit in toc -->
#### Avant de soumettre un rapport de bogue

Un bon rapport de bogue ne doit pas laisser les autres chercher des informations supplémentaires. Nous vous demandons donc de faire des recherches attentives, de collecter des informations et de décrire le problème en détail dans votre rapport. Veuillez effectuer les étapes suivantes à l'avance pour nous aider à corriger tout bogue potentiel aussi rapidement que possible.

- Assurez-vous d'utiliser la dernière version.
- Déterminez si votre bogue est vraiment un bogue et non une erreur de votre part, par exemple en utilisant des composants ou des versions d'environnement incompatibles (assurez-vous d'avoir lu la [documentation](https://github.com/KoroKira/Cours-CommunistIcam/blob/main/documentation.md). Si vous cherchez du support, vous voudrez peut-être vérifier [cette section](#i-have-a-question)).
- Pour voir si d'autres utilisateurs ont rencontré (et potentiellement déjà résolu) le même problème que vous, vérifiez s'il existe déjà un rapport de bogue pour votre bogue ou erreur dans le [bug tracker](https://github.com/KoroKira/Cours-CommunistIcam/issues?q=label%3Abug).
- Assurez-vous également de rechercher sur Internet (y compris Stack Overflow) pour voir si des utilisateurs en dehors de la communauté GitHub ont discuté du problème.
- Collectez des informations sur le bogue :
- Trace de la pile (traceback)
- Système d'exploitation, plateforme et version (Windows, Linux, macOS, x86, ARM)
- Version de l'interpréteur, du compilateur, du SDK, de l'environnement d'exécution, du gestionnaire de packages, selon ce qui semble pertinent.
- Éventuellement, votre entrée et la sortie
- Pouvez-vous reproduire le problème de manière fiable ? Et pouvez-vous également le reproduire avec des versions plus anciennes ?

<!-- omit in toc -->
#### Comment soumettre un bon rapport de bogue ?

> Vous ne devez jamais signaler des problèmes liés à la sécurité, des vulnérabilités ou des bugs contenant des informations sensibles sur le bug tracker ou ailleurs en public. Au lieu de cela, les bugs sensibles doivent être envoyés par courriel à <>.
<!-- Vous pouvez ajouter une clé PGP pour permettre l'envoi des messages de manière chiffrée également. -->

Nous utilisons les issues GitHub pour suivre les bugs et erreurs. Si vous rencontrez un problème avec le projet :

- Ouvrez une [Issue](https://github.com/KoroKira/Cours-CommunistIcam/issues/new). (Étant donné que nous ne pouvons pas être sûrs à ce stade s'il s'agit d'un bogue ou non, nous vous demandons de ne pas parler d'un bogue et de ne pas étiqueter l'issue.)
- Expliquez le comportement que vous attendez et le comportement réel.
- Fournissez autant de contexte que possible et décrivez les *étapes de reproduction* qu'une autre personne peut suivre pour recréer le problème de manière indépendante. Cela inclut généralement votre code. Pour de bons rapports de bogues, vous devez isoler le problème et créer un cas de test réduit.
- Fournissez les informations que vous avez collectées dans la section précédente.

Une fois l'issue ouverte :

- L'équipe du projet étiquettera l'issue en conséquence.
- Un membre de l'équipe tentera de reproduire le problème avec les étapes que vous avez fournies. S'il n'y a pas d'étapes de reproduction ou aucune façon évidente de reproduire le problème, l'équipe vous demandera ces étapes et marquera l'issue comme `needs-repro`. Les bogues avec l'étiquette `needs-repro` ne seront pas traités tant qu'ils ne seront pas reproduits.
- Si l'équipe parvient à reproduire le problème, il sera marqué `needs-fix`, ainsi que éventuellement d'autres étiquettes (telles que `critical`), et l'issue sera laissée à [implémenter par quelqu'un](#your-first-code-contribution).

<!-- Vous voudrez peut-être créer un modèle d'issue pour les bogues et les erreurs qui peut être utilisé comme guide et qui définit la structure des informations à inclure. Si vous le faites, référencez-le ici dans la description. -->


### Suggérer des améliorations

Cette section vous guide à travers la soumission d'une suggestion d'amélioration pour Cours-CommunistIcam, **y compris les nouvelles fonctionnalités et les améliorations mineures de la fonctionnalité existante**. Suivre ces directives aidera les mainteneurs et la communauté à comprendre votre suggestion et à trouver des suggestions connexes.

<!-- omit in toc -->
#### Avant de soumettre une amélioration

- Assurez-vous d'utiliser la dernière version.
- Lisez attentivement la [documentation](https://github.com/KoroKira/Cours-CommunistIcam/blob/main/documentation.md) et découvrez si la fonctionnalité est déjà couverte, peut-être par une configuration individuelle.
- Effectuez une [recherche](https://github.com/KoroKira/Cours-CommunistIcam/issues) pour voir si l'amélioration a déjà été suggérée. Si c'est le cas, ajoutez un commentaire à l'issue existante au lieu d'en ouvrir une nouvelle.
- Découvrez si votre idée correspond à la portée et aux objectifs du projet. C'est à vous de faire valoir le bien-fondé de cette fonctionnalité aux développeurs du projet. Gardez à l'esprit que nous voulons des fonctionnalités qui seront utiles à la majorité de nos utilisateurs et pas seulement à une petite partie. Si vous ciblez simplement une minorité d'utilisateurs, envisagez d'écrire une bibliothèque d'extension/plugin.

<!-- omit in toc -->
#### Comment soumettre une bonne suggestion d'amélioration ?

Les suggestions d'amélioration sont suivies sous forme [d'issues GitHub](https://github.com/KoroKira/Cours-CommunistIcam/issues).

- Utilisez un **titre clair et descriptif** pour l'issue afin d'identifier la suggestion.
- Fournissez une **description étape par étape de l'amélioration suggérée** aussi en détail que possible.
- **Décrivez le comportement actuel** et **expliquez quel comportement vous vous attendiez à voir à la place** et pourquoi. À ce stade, vous pouvez également indiquer quelles alternatives ne fonctionnent pas pour vous.
- Vous voudrez peut-être **inclure des captures d'écran et des GIF animés** qui vous aident à démontrer les étapes ou à indiquer la partie à laquelle la suggestion est liée. Vous pouvez utiliser [cet outil](https://www.cockos.com/licecap/) pour enregistrer des GIF sur macOS et Windows, et [cet outil](https://github.com/colinkeenan/silentcast) ou [cet outil](https://github.com/GNOME/byzanz) sur Linux. <!-- cela ne devrait être inclus que si le projet a une interface graphique -->
- **Expliquez pourquoi cette amélioration serait utile** pour la plupart des utilisateurs de Cours-CommunistIcam. Vous voudrez peut-être également mentionner les autres projets qui l'ont mieux résolu et qui pourraient servir d'inspiration.

<!-- Vous voudrez peut-être créer un modèle d'issue pour les suggestions d'amélioration qui peut être utilisé comme guide et qui définit la structure des informations à inclure. Si vous le faites, référencez-le ici dans la description. -->

### Votre Première Contribution de Code
<!-- TODO
Inclure la configuration de l'environnement, de l'IDE et les instructions typiques pour commencer !

-->

### Améliorer la Documentation
<!-- TODO
Mise à jour, amélioration et correction de la documentation

-->

## Guides de Style
### Messages de Validation (Commit)
<!-- TODO

-->

## Rejoindre l'Équipe du Projet
<!-- TODO -->

<!-- omit in toc -->
