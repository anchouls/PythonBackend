import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from .models import symptoms, patients


class Symptom(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

    def resolve_name(self, info):
        return symptoms[self.id]


class Patient(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    disease = graphene.String()
    symptoms = graphene.List(Symptom)

    def resolve_name(self, info):
        return patients[self.id]['name']

    def resolve_disease(self, info):
        return patients[self.id]['disease']

    def resolve_symptoms(self, info):
        answer = list()
        for i in patients[self.id]['symptoms']:
            symptom = Symptom()
            symptom.id = i
            answer.append(symptom)
        return answer


class Query(graphene.ObjectType):
    me = graphene.Field(Patient)
    my_friend = graphene.Field(Patient)
    my_pet = graphene.Field(Patient)

    @staticmethod
    def resolve_me(self, info):
        patient = Patient()
        patient.id = 1
        return patient

    @staticmethod
    def resolve_my_friend(self, info):
        patient = Patient()
        patient.id = 2
        return patient

    @staticmethod
    def resolve_my_pet(self, info):
        patient = Patient()
        patient.id = 3
        return patient


app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
