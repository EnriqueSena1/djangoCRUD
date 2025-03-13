from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from api.views.apiViews import *
from api.views.webViews import *

# router = DefaultRouter()
# router.register('funcionarios', FuncionarioViewSet)
# router.register('produtos', ProdutoViewSet)
# router.register('categorias', CategoriaViewSet)
# router.register('alunos', AlunoViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('api/user', User.as_view(), name="usuarios"),
    path('api/user/<int:id>', User.as_view(), name="usuarioDetalhe"),
    path('api/login', Login.as_view(), name="loginAPI"),
    path('home/', home, name="home"),
    path('login/', login, name="login"),
    path('criarAluno/', criarAluno, name="criarAluno"),

    # path('funcionarios/', listarFuncionarios, name='listarFuncionarios'),
    # path('funcionarios/cadastrar', cadastrarFuncionario, name='cadastrarFuncionario'),
    # path('funcionarios/<int:id>', obterFuncionario, name='obterFuncionario'),

]