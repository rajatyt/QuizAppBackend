from django.shortcuts import render
from rest_framework import generics
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuizSerializer, QuestionQuizSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer


class RandomQuiz(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs[
            'topic']).order_by('?')[:1]
        serializer = RandomQuizSerializer(question, many=True)
        return Response(serializer.data)


class QuestionQuiz(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionQuizSerializer(question, many=True)
        return Response(serializer.data)
