from django.db import models

# Create your models here.


# Contraintes dans les champs du model. on définit la fonction et on l'ajoute à un champ du model via le paramètre 'validators'
from django.core.exceptions import ValidationError
from string import ascii_uppercase, digits
  
def lettres_majuscule(expression):
    for i in expression:
        if i not in ascii_uppercase:
            raise ValidationError('%(expression)s doit etre en majuscule et contenir uniquement des lettres',params={'expression':expression},)

def age_2_chiffres(expression):
    if len(str(expression)) > 2:
        raise ValidationError("L'age doit etre composé de 2 chiffres",params={'expression':expression},)

def numero1_8chiffres(expression):
    if len(str(expression)) != 8:
        raise ValidationError("Le numéro de téléphone doit etre composé de 8 chiffres",params={'expression':expression},)

def numero2_8chiffres(expression):
    if len(str(expression)) != 8:
        raise ValidationError("Le numéro de téléphone doit etre composé de 8 chiffres",params={'expression':expression},)

def code_16caracteres(expression):
    if len(expression) != 16:
        raise ValidationError("Le code du patient doit etre composé de 16 caractères",params={'expression':expression},)
    #elif [int(i) not in digits for i in list(expression[:4])]:
        #raise ValidationError("Le code du centre doit etre composé uniquement de chiffres",params={'expression':expression},)
    #elif expression[4] !="/":
        #raise ValidationError("Le code du centre et le numéro du site doivent etre séparer par /",params={'expression':expression},)
    #elif [int(j) not in digits for j in list(expression[5:7])]:
        #raise ValidationError("Le numéro du site doit etre composé uniquement de chiffres",params={'expression':expression},)
    #elif expression[7] !="/":
        #raise ValidationError("Le numéro du site et l'année doivent etre séparer par /",params={'expression':expression},)
    #elif [int(k) not in digits for k in list(expression[8:10])]:
        #raise ValidationError("L'année doit etre composé uniquement de chiffres",params={'expression':expression},)
    #elif expression[10] !="/":
        #raise ValidationError("L'année et le numéro du patient doivent etre séparer par /",params={'expression':expression},)
    #elif [int(l) not in digits for l in list(expression[11:])]:
        #raise ValidationError("Le numéro du patient doit etre composé uniquement de chiffres",params={'expression':expression},)



class Patient(models.Model):
    code_patient=models.CharField('Code du patient',unique=True,max_length=16,primary_key=True,validators=[code_16caracteres])
    nom=models.CharField('Nom',unique=False,max_length=30,validators=[lettres_majuscule])
    prenom=models.CharField('Prénom',unique=True,max_length=100,validators=[lettres_majuscule])
    sexe=models.CharField('Sexe',max_length=10,choices=[('M','Masculin'),('F','Féminin')])
    age=models.IntegerField('Age',null=True,validators=[age_2_chiffres])
    numero1=models.IntegerField('Numéro de tel. 1',null=True,validators=[numero1_8chiffres])
    numero2=models.IntegerField('Numéro de tel. 2',blank=True,null=True, validators=[numero2_8chiffres])
    date_enrol=models.DateField("Date d'enrollement",null=True)
    porte_entrer=models.CharField("Porte d'entrée",max_length=50,choices=[('PTME','PTME'),('CDV','CDV'),('MEDECINE','MEDECINE'),('INDEX TESTING','INDEX TESTING'),('MATERNITE','MATERNITE'),('COMMUNAUTE','COMMUNAUTE'),('TRANSFERT IN','TRANSFERT IN')])
    #nom_parrain=models.ForeignKey(Parrain_marraine,on_delete=models.CASCADE)
    parrain_marraine=models.CharField('Parrain/Marraine',max_length=50,choices=[('AHEMOU','AHEMOU'),('DIANE','DIANE'),('ELIANE','ELIANE'),('ESTELLE','ESTELLE'),('MAMBO','MAMBO'),('LARISSA','LARISSA')])
    observation=models.CharField('Observation',blank=True,max_length=300,null=True)