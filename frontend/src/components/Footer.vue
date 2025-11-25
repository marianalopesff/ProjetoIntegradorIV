<template>
    <footer class="bg-white py-12 shadow-[0_-5px_10px_rgba(0,0,0,0.05)]">
        <div class="max-w-7xl mx-auto px-6">
            <!-- Troque o grid por flex para 3 colunas -->
            <div class="flex flex-col md:flex-row justify-between gap-8">
                <!-- Sobre a empresa -->
                <div class="md:w-1/4">
                    <h3 class="text-lg font-bold text-gray-900 mb-4 font-montserrat">PROJETO INTEGRADOR IV</h3>
                    <p class="text-gray-700 text-sm font-montserrat">
                        O projeto consiste em desenvolver uma aplicação web capaz de receber contratos de software,
                        aplicativos ou serviços online (EULAs, termos de uso, políticas de privacidade) e gerar
                        automaticamente: resumo em linguagem simples e destaque de riscos.
                    </p>
                </div>

                <!-- Contato -->
                <div class="md:w-1/4">
                    <h3 class="text-lg font-bold text-gray-900 mb-4 font-montserrat hover:text-gray-700">INTEGRANTES
                    </h3>
                    <ul class="space-y-2 text-sm text-gray-700 font-montserrat tracking-wide">
                        <div class="flex gap-2">
                            <UserRound size="18" />
                            <li>Lucas Fraga Xavier</li>
                        </div>

                        <div class="flex gap-2">
                            <UserRound size="18" />
                            <li>Jordhan Fernandes de Assis</li>
                        </div>

                        <div class="flex gap-2">
                            <UserRound size="18" />
                            <li>Mariana Lopes Ferreira</li>
                        </div>

                        <div class="flex gap-2">
                            <UserRound size="18" />
                            <li>Rogelio Soares Reis Filho</li>
                        </div>

                        <div class="flex gap-2">
                            <UserRound size="18" />
                            <li>Murilo da Silva Soares</li>
                        </div>

                    </ul>
                </div>

                <!-- Redes sociais -->
                <!-- Principais Tecnologias / Linguagens Utilizadas -->
                <div class="md:w-1/4">
                    <h3 class="text-lg font-bold text-gray-900 mb-4 font-montserrat">PRINCIPAIS TECNOLOGIAS / LINGUAGENS
                        UTILIZADAS</h3>
                    <div class="grid grid-cols-2 gap-x-6 gap-y-2 text-sm text-gray-700 font-montserrat tracking-wide">
                        <span>Vue.js</span>
                        <span>Tailwind CSS</span>
                        <span>Python</span>
                        <span>Flask</span>
                        <span>Flask-CORS</span>
                        <span>PyTorch</span>
                        <span>Transformers</span>
                        <span>deep-translator</span>
                        <span>Pandas</span>
                        <span>Axios</span>
                        <span>scikit-learn</span>
                        <span>Regex</span>
                        <span>KaggleHub</span>
                        <span>HTML5/CSS3</span>
                        <span>Vite</span>
                        <span>API REST</span>
                    </div>
                </div>

            </div>

            <!-- Direitos autorais -->
            <div
                class="mt-12 pt-6 border-t border-gray-200 text-center text-sm text-gray-500 font-montserrat tracking-wide">
                <p>© 2025 Trabalho de Projeto Integrador IV.</p>
            </div>
        </div>
    </footer>


</template>


<script setup>
import { Instagram, Facebook, MapPinned, Mail, UserRound } from 'lucide-vue-next';
</script>