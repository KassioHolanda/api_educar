from rest_framework import serializers

from grade.models import Disciplina, GradeCurso, SerieDisciplina, AnoLetivo, DisciplinaAluno, SituacaoTurmaMes


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = 'id', 'descricao', 'codigo'


class GradeCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeCurso
        fields = 'id', 'professor', 'seriedisciplina', 'turma', 'disciplina'


class SerieDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieDisciplina
        fields = 'id', 'disciplina', 'serie'


class AnoLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnoLetivo
        fields = 'id', 'descricao', 'datafinal', 'datainicio', 'fechadonota'


class DisciplinaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaAluno
        fields = '__all__'


class SituacaoTurmaMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacaoTurmaMes
        fields = '__all__'
