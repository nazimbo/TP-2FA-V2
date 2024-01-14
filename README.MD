### Installation :

1. **Cloner le Repository :**

   ```bash
   git clone git@github.com:nazimbo/TP-2FA-V2.git
   cd TP-2FA-V2
   ```

2. **Installer les Dépendances :**

   ```bash
   pip install flask flask-wtf pyotp qrcode wtforms
   ```

3. **Lancer l'Application :**
   ```bash
   python app.py
   ```

### Utilisation :

1. **Accéder au Site :**
   Ouvrez votre navigateur web et accédez à [http://localhost:5000/]

2. **Connexion avec Mot de Passe Prédéfini :**

   - Saisissez un nom d'utilisateur.
   - Entrez le mot de passe prédéfini (actuellement défini comme "password").
   - Appuyez sur le bouton "Login".

3. **Activation de l'Authentification à Deux Facteurs (2FA) :**

   - Si le mot de passe est correct, l'application générera un QR code.
   - Scannez le QR code avec une application compatible (par exemple, FreeOTP) ou entrez manuellement le code fourni.

4. **Vérification de l'Authentification à Deux Facteurs :**

   - Utilisez l'application 2FA pour générer un code de vérification.
   - Saisissez le code dans le champ prévu.
   - Appuyez sur le bouton "Verify".

5. **Résultats de la Vérification :**
   - Si le code est correct, le site affichera "Verification réussie ! Vous pouvez maintenant utiliser le 2FA;"
   - Sinon, un message d'erreur s'affichera, vous invitant à réessayer.
