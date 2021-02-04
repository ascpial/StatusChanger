# Discord StatusChanger

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
![license](https://img.shields.io/badge/LICENSE-MIT-1?style=for-the-badge)

## Présentation

Ce programme permet de créer des status avancés personnalisés tels que celui ci sur discord :

![small_profil](assets/small_profil_example.png)

![large_profil](assets/large_profil_example.png)

Il utilise le [client RPC de discord](https://discord.com/developers/docs/topics/rpc) et une interface très simple :

![preview](assets/application_preview.png)

## Prérequis

Vous devez avoir un compte discord sur l'application bureau et un [id d'application discord](https://discord.com/developers/applications) (référez vous à la section `Créez votre propre jeu`).

Après avoir installé et lancé l'application, cette interface apparaît :

> Une traduction en français est disponible sur la première fenêtre

![first_interface](assets/first_interface.png)

Mettez votre ID d'application dans le champs de saisie et sélectionnez `Continuer`.

Cette nouvelle interface apparaît et je vous invite à aller voir la [documentation discord](https://discord.com/developers/docs/rich-presence/how-to#updating-presence-update-presence-payload-fields) pour savoir à quoi correspondent chaque champ.

![preview](assets/application_preview.png)

> Pour envoyer votre riche presence, appuyez sur `Envoyer`. Si vous voulez retirer votre status sans fermer l'application, appuiez sur `Effacer`. Pour sauvegarder votre configuration sans envoyer le rich presence, appuiyez sur `Sauvegarder`

## Créez votre propre jeu

Pour changer le nom du jeu auquel vous jouez, vous devez créer une application sur la page de [développement de discord](https://discord.com/developers/applications).

Créez une application :

![create_application](assets/create_application.png)

Le nom demandé sera le nom du jeu que vous allez créer. Il est modifiable après la création.

![name](assets/ask_name.png)

Après la création de l'application, vous pouvez lui donner un logo.

Pour pouvoir utiliser votre jeu dans l'application, copiez votre ID d'application et collez le sur la première fenêtre de l'application :

![copy_id](assets/copy_id.png)
![past_id](assets/past_id.png)

 Allez ensuite dans l'onglet `Rich Presence` :

![rich_presence](assets/rich_presence.png)

Vous pouvez ajouter ici le logo par défaut du jeu.
Vous pouvez aussi ajouter des images supplémentaires avec la section `Rich Presence Assets`, où vous pouvez ajouter des images (attention parfois celà peut prendre du temps avant que discord prenne en compte vos modifications) que vous pourrez utiliser avec les champs de saisie `Large Image Key` et `Small Image Key` de l'application.