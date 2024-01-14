def traduire_erreurs(erreur):
    """Traduit les erreurs de validation en français.

    Args:
        erreurs (str): Une erreur de validation.

    Returns:
        str: L'erreur traduite.
    """
    if erreur == "This field is required.":
        return "Ce champ est obligatoire"
    elif erreur == "Invalid email address.":
        return "Adresse email invalide"
    elif erreur == "Field must be equal to mdp.":
        return "Les mots de passe ne correspondent pas"
    elif erreur == "Password must be at least 8 characters long.":
        return "Le mot de passe doit contenir au moins 8 caractères"
    else:
        return erreur