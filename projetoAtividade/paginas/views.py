from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cidade, Pessoa, Setor, Atividade, Demanda

class index(TemplateView):
    template_name = 'paginas/index.html'

class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class SetorCreate(LoginRequiredMixin, CreateView):
    model = Setor
    fields = ['nome',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class AtividadeCreate(LoginRequiredMixin, CreateView):
    model = Atividade
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class DemandaCreate(LoginRequiredMixin, CreateView):
    model = Demanda
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento','cidade']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('listar-pessoa')


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class SetorUpdate(LoginRequiredMixin, UpdateView):
    model = Setor
    fields = ['nome',
              'area_atuacao',
              'email']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class AtividadeUpdate(LoginRequiredMixin, UpdateView):
    model = Atividade
    fields = ['titulo',
              'data_entrega',
              'status',
              'is_urgente',
              'descricao',
              'setor']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')


class DemandaUpdate(LoginRequiredMixin, UpdateView):
    model = Demanda
    fields = ['titulo',
              'data_inicial',
              'data_final',
              'og',
              'lista_de_atividades']
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('index')

#=##############


class DemandaDelete(LoginRequiredMixin, DeleteView):
    model = Demanda
    template_name = 'cadastros/form-delete.html'
    sucess_url = reverse_lazy('index')
    

class AtividadeDelete(LoginRequiredMixin, DeleteView):
    model = Atividade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class SetorDelete(LoginRequiredMixin, DeleteView):
    model = Setor
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class CidadeDelete(LoginRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('index')


class PessoaDelete(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'paginas/form-delete.html'
    success_url = reverse_lazy('listar-pessoa')


class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'paginas/listas/pessoa.html'