<template>
    <div id="background" class="min-h-screen bg-[#EBF6F7]">
        <section id="aba2">
            <div class="max-w-6xl mx-auto px-6 pt-32 scroll-mt-32 font-montserrat">
                <!-- Título principal -->
                <div class="bg-white rounded-xl shadow-lg p-8 mb-8">
                    <div class="flex items-center gap-3 mb-4">
                        <CodeXml class="text-blue-600" :size="42" />
                        <h1 class="text-3xl font-bold text-gray-800">Projeto Integrador IV</h1>
                    </div>
                    <h2 class="text-xl font-semibold text-blue-700 mb-2">EULA Simplificado – Analisador Automático de
                        Termos de Uso e Políticas de Privacidade</h2>
                </div>

                <!-- Descrição -->
                <div class="grid md:grid-cols-2 gap-8 mb-8">
                    <div class="bg-white rounded-xl shadow p-7">
                        <h3 class="text-lg font-bold text-gray-900 mb-2 flex items-center gap-2">
                            <Sun :size="20" class="text-blue-500" />Descrição do Projeto
                        </h3>
                        <p class="text-gray-700 mb-3">
                            O projeto consiste em desenvolver uma aplicação web capaz de receber contratos de software,
                            aplicativos ou serviços online (EULAs, termos de uso, políticas de privacidade) e gerar
                            automaticamente:
                        </p>
                        <ul class="list-disc ml-5 text-gray-800 mb-1">
                            <li><span class="font-semibold">Resumo em linguagem simples</span>, facilitando a
                                compreensão do usuário;</li>
                            <li><span class="font-semibold">Destaque de riscos em categorias específicas:</span>
                                <ul class="list-disc ml-4">
                                    <li>Coleta e compartilhamento de dados pessoais</li>
                                    <li>Cobranças automáticas ou escondidas</li>
                                    <li>Compartilhamento de informações com terceiros</li>
                                    <li>Jurisdição ou obrigações legais</li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                    <!-- Grupo / Integrantes -->
                    <div class="bg-white rounded-xl shadow p-7">
                        <h3 class="text-lg font-bold text-gray-900 mb-2 flex items-center gap-2">
                            <UserRound :size="20" class="text-green-600" />Grupo
                        </h3>
                        <ul class="text-gray-800 space-y-2">
                            <li class="flex items-center gap-2">
                                <UserRound :size="16" class="text-blue-400" />Rogelio Soares
                            </li>
                            <li class="flex items-center gap-2">
                                <UserRound :size="16" class="text-blue-400" />Mariana Lopes
                            </li>
                            <li class="flex items-center gap-2">
                                <UserRound :size="16" class="text-blue-400" />Jordhan Fernandes
                            </li>
                            <li class="flex items-center gap-2">
                                <UserRound :size="16" class="text-blue-400" />Murilo da Silva
                            </li>
                            <li class="flex items-center gap-2">
                                <UserRound :size="16" class="text-blue-400" />Lucas Xavier
                            </li>
                        </ul>
                    </div>
                </div>

                <!-- Justificativa -->
                <div class="bg-white rounded-xl shadow p-7 mb-8">
                    <h3 class="text-lg font-bold text-gray-900 mb-2 flex items-center gap-2">
                        <Sun :size="20" class="text-yellow-400" />Justificativa do Tema
                    </h3>
                    <p class="mb-2 text-gray-700">
                        A maioria dos usuários aceita contratos sem ler devido à linguagem técnica e extensão dos
                        documentos, ficando vulnerável à coleta excessiva de dados e cobranças inesperadas.
                    </p>
                    <p class="mb-2 text-gray-700">
                        Um sistema automatizado que simplifique os termos e destaque riscos ajuda a:
                    </p>
                    <ul class="list-disc ml-5 text-gray-800">
                        <li>Aumentar a consciência digital dos usuários</li>
                        <li>Reduzir incidentes de exposição de dados</li>
                        <li>Proporcionar transparência em serviços digitais</li>
                    </ul>
                </div>

                <!-- Métricas de Impacto & Sociedade Impactada -->
                <div class="grid md:grid-cols-2 gap-8 mb-8">
                    <div class="bg-white rounded-xl shadow p-7">
                        <h3 class="text-lg font-bold text-gray-900 mb-2">Métricas de Impacto</h3>
                        <ul class="list-disc ml-5 text-gray-800">
                            <li>Número de contratos analisados</li>
                            <li>Quantidade de riscos detectados e destacados</li>
                            <li>Feedback dos usuários sobre clareza e utilidade do resumo</li>
                            <li>Tempo economizado na leitura de contratos</li>
                        </ul>
                    </div>
                    <div class="bg-white rounded-xl shadow p-7">
                        <h3 class="text-lg font-bold text-gray-900 mb-2">Sociedade Impactada</h3>
                        <ul class="list-disc ml-5 text-gray-800 mb-3">
                            <li>
                                <span class="font-semibold">Usuários digitais:</span> alunos, profissionais e
                                consumidores de apps e serviços online
                            </li>
                            <li>
                                <span class="font-semibold">Pequenos negócios e startups:</span> ao contratar serviços
                                ou analisar EULAs de fornecedores
                            </li>
                            <li>
                                <span class="font-semibold">Instituições de ensino e serviços digitais:</span> avaliação
                                de termos de uso internos
                            </li>
                        </ul>
                        <p class="text-gray-700 mt-2">
                            <span class="font-semibold">Impacto:</span> maior compreensão e proteção legal/privacidade,
                            reduzindo riscos de abuso e garantindo acessibilidade.
                        </p>
                    </div>
                </div>

                <!-- Ferramentas e Tecnologias -->
                <div class="bg-white rounded-xl shadow p-7 mb-8">
                    <h3 class="text-lg font-bold text-gray-900 mb-2 flex items-center gap-2">
                        <Sun :size="20" class="text-blue-600" />Ferramentas e Tecnologias
                    </h3>
                    <div class="grid grid-cols-2 md:grid-cols-3 gap-2 text-gray-700 text-sm">
                        <span>Hugging Face Transformers</span>
                        <span>PyTorch</span>
                        <span>DistilBERT</span>
                        <span>Deep Translator</span>
                        <span>Pandas</span>
                        <span>Regex</span>
                        <span>scikit-learn</span>
                        <span>Flask</span>
                        <span>Vue.js</span>
                        <span>Tailwind CSS</span>
                        <span>Kaggle – ToS;DR Corpus</span>
                    </div>
                </div>

                <!-- Funcionamento do Sistema -->
                <div class="bg-white rounded-xl shadow p-7 mb-8">
                    <h3 class="text-lg font-bold text-gray-900 mb-2 flex items-center gap-2">
                        <Sun :size="20" class="text-violet-600" />Resumo do Funcionamento
                    </h3>
                    <p class="text-gray-700 mb-2">
                        O sistema integra Inteligência Artificial, tradução automática e interface web para facilitar a
                        compreensão dos principais riscos e pontos de atenção em contratos e políticas.
                    </p>
                    <div class="mb-3">
                        <h4 class="font-semibold text-gray-800 mb-1">Etapas do Processo:</h4>
                        <ol class="list-decimal ml-5 text-gray-800">
                            <li><span class="font-bold">Entrada do Texto:</span> usuário insere o texto do contrato</li>
                            <li><span class="font-bold">Pré-processamento:</span> limpeza e padronização</li>
                            <li><span class="font-bold">Tradução Automática:</span> texto traduzido para inglês</li>
                            <li><span class="font-bold">Análise com IA:</span> modelo classifica nível de risco</li>
                            <li><span class="font-bold">Exibição dos Resultados:</span> pontos destacados na interface
                            </li>
                        </ol>
                    </div>
                    <div class="mb-3">
                        <h4 class="font-semibold text-gray-800 mb-1">Fluxo Simplificado:</h4>
                        <div class="flex flex-col gap-2 text-gray-900">
                            <span>Usuário</span>
                            <span class="text-2xl text-blue-400 font-bold">↓</span>
                            <span>Interface Web (Flask) - Protótipo</span>
                            <span class="text-2xl text-blue-400 font-bold">↓</span>
                            <span>Pré-processamento e Tradução</span>
                            <span class="text-2xl text-blue-400 font-bold">↓</span>
                            <span>Modelo de IA (Transformers + PyTorch)</span>
                            <span class="text-2xl text-blue-400 font-bold">↓</span>
                            <span>Classificação do Texto</span>
                            <span class="text-2xl text-blue-400 font-bold">↓</span>
                            <span>Resultado e Resumo exibidos ao usuário</span>
                        </div>
                    </div>
                </div>

                <!-- Tutorial e Links -->
                <div class="grid md:grid-cols-2 gap-8 mb-4">
                    <div class="bg-white rounded-xl shadow p-7">
                        <h3 class="text-lg font-bold text-gray-900 mb-2 flex items-center gap-2">
                            <Sun :size="20" class="text-blue-400" />Tutorial de Instalação
                        </h3>
                        <ul class="list-disc ml-5 text-gray-800 space-y-1">
                            <li>Para instalar as dependências do backend (Python): <span
                                    class="font-mono bg-blue-50 px-2 py-1 rounded">pip install -r
                                    requirements.txt</span></li>
                            <li>Para instalar as dependências do frontend, rode dentro da pasta frontend: <span
                                    class="font-mono bg-blue-50 px-2 py-1 rounded">npm install axios</span></li>
                        </ul>
                    </div>
                    <div class="bg-white rounded-xl shadow p-7">
                        <h3 class="text-lg font-bold text-gray-900 mb-2 flex items-center gap-2">
                            <Sun :size="20" class="text-rose-400" />Links Úteis
                        </h3>
                        <ul class="list-disc ml-5 text-blue-700 space-y-2">
                            <li>
                                <a href="https://www.kaggle.com/datasets/sonu1607/tosdr-terms-of-service-corpus"
                                    target="_blank" class="underline hover:text-blue-600">
                                    Dataset: ToSDR Terms of Service Corpus
                                </a>
                            </li>
                            <li>
                                <a href="https://youtu.be/t9gtAb8C5UM" target="_blank"
                                    class="underline hover:text-blue-600">
                                    Apresentação Protótipo (YouTube)
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <br><br><br>
        </section>
    </div>
</template>

<script setup>
import { CodeXml, UserRound } from 'lucide-vue-next'
</script>

<style scoped>
.font-montserrat {
    font-family: 'Montserrat', sans-serif !important;
}
</style>
