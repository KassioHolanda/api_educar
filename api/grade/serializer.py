from rest_framework import serializers

from grade.models import Disciplina, GradeCurso, SerieDisciplina, AnoLetivo, DisciplinaAluno, SituacaoTurmaMes


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = 'id', 'descricao', 'codigo'


class GradeCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeCurso
        fields = '__all__'


class SerieDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieDisciplina
        fields = '__all__'


class AnoLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnoLetivo
        fields = '__all__'


class DisciplinaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaAluno
        fields = '__all__'


class SituacaoTurmaMesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacaoTurmaMes
        fields = '__all__'
