from rest_framework import serializers

from grade.models import Disciplina, GradeCurso, SerieDisciplina, AnoLetivo, DisciplinaAluno, SituacaoTurmaMes


class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplina
        fields = 'id', 'descricao', 'codigo'


class GradeCursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GradeCurso
        fields = 'id', 'professor', 'seriedisciplina', 'turma', 'disciplina'


class SerieDisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SerieDisciplina
        fields = 'id', 'serie', 'disciplina'


class AnoLetivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnoLetivo
        fields = 'id', 'datafinal', 'datainicio', 'fechadonota'


class DisciplinaAlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisciplinaAluno
        fields = 'id', 'cargahoraria', 'statusdisciplinaaluno', 'statusatual', 'matricula', 'seriedisciplina', 'mediaacumulada', 'mesesfechadonota', 'notaacumulada', 'datacadastroprovafinal', 'notaprovafinal',
        'fechadoprovafinal', 'datacadastroatualizacaoprovafinal', 'notaantigaprovafinal', 'usuarioatualizacaoprovafinal'


class SituacaoTurmaMesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SituacaoTurmaMes
        fields = 'id', 'datahora', 'status', 'turma', 'quantidadeaprovados', 'quantidadereprovados', 'bimestre'
