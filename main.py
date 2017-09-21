import falcon
from resources.equipamento_api import EquipamentoResource
from resources.aluno_api import AlunoResource
from resources.emprestimo_api import EmprestimoResource
from resources.ponto_api import PontoResources
from resources.projeto_api import ProjetoResources
from resources.time_api import TimeResources
from resources.time_aluno_api import TimeAlunoResources
from resources.aluno_projeto_api import AlunoProjetoResources

app = falcon.API()
app.add_route('/equipamentos', EquipamentoResource())
app.add_route('/alunos', AlunoResource())
app.add_route('/emprestimos', EmprestimoResource())
app.add_route('/pontos', PontoResources())
app.add_route('/projetos', ProjetoResources())
app.add_route('/times', TimeResources())
app.add_route('/time_aluno', TimeAlunoResources())
app.add_route('/aluno_projeto', AlunoProjetoResources())