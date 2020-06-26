from django.db import models
import datetime
# Create your models here.


# Contraintes dans les champs du model. on définit la fonction et on l'ajoute à un champ du model via le paramètre 'validators'
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from string import ascii_uppercase, digits
import re
  
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
    if not re.match(r'^[0-9]{4}\/[0-9]{2}\/[0-9]{2}\/[0-9]{5}',expression):
        raise ValidationError("Le format du code patient est incorrect!",params={'expression':expression},)


class Parrain(models.Model):
    libelle=models.CharField('Libéllé',max_length=100)

    def __str__(self):
        return self.libelle

		
class Patient(models.Model):
    code_patient=models.CharField('Code du patient',unique=True,max_length=16,primary_key=True,help_text='____/__/__/_____',validators=[code_16caracteres])
    nom=models.CharField('Nom',unique=False,max_length=30,validators=[lettres_majuscule])
    prenom=models.CharField('Prénom',unique=True,max_length=100,validators=[lettres_majuscule])
    sexe=models.CharField('Sexe',max_length=10,choices=[('M','Masculin'),('F','Féminin')])
    age=models.IntegerField('Age',null=True,validators=[age_2_chiffres])
    numero1=models.IntegerField('Numéro de tel. 1',null=True,validators=[numero1_8chiffres])
    numero2=models.IntegerField('Numéro de tel. 2',blank=True,null=True, validators=[numero2_8chiffres])
    date_enrol=models.DateField("Date d'enrollement",null=True,validators = [MaxValueValidator(datetime.datetime.now().date())])
    porte_entrer=models.CharField("Porte d'entrée",max_length=50,choices=[('PTME','PTME'),('CDV','CDV'),('MEDECINE','MEDECINE'),('INDEX TESTING','INDEX TESTING'),('MATERNITE','MATERNITE'),('COMMUNAUTE','COMMUNAUTE'),('TRANSFERT IN','TRANSFERT IN')])
    parrain=models.ForeignKey(Parrain,on_delete=models.SET_NULL,blank=True,null=True,related_name='patients')
    observation=models.CharField('Observation',blank=True,max_length=300,null=True)

    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)


    @property
    def cohorte_actuelle(self):
        today=datetime.datetime.now()
        diff_mois=(today.year-self.date_enrol.year) *12+today.month-self.date_enrol.month+1 # pylint: disable=no-member
        return "M{}".format(str(diff_mois))

    
	
        
        
		
		
		

