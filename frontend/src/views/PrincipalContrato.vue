<template>
    <div class="min-h-screen bg-[#EBF6F7] flex flex-col font-montserrat">
        <div class="flex-grow flex items-center justify-center">
            <div class="bg-white rounded-xl shadow-lg p-8 w-full max-w-lg mx-auto text-center">
                <div class="flex justify-center items-center mb-5 gap-2">
                    <ScrollText :size="32" class="text-blue-700" />
                    <h1 class="text-2xl font-semibold text-blue-700">EULA Simplificado</h1>
                </div>
                <div class="flex flex-col gap-4">
                    <textarea v-model="contrato" placeholder="Cole o contrato ou política de privacidade aqui..."
                        class="resize-y border border-blue-200 rounded-lg p-4 min-h-[140px] text-base focus:outline-none focus:ring-2 focus:ring-blue-200 transition"></textarea>
                    <button @click="analisarContrato" :disabled="loading"
                        class="bg-blue-600 hover:bg-blue-700 disabled:bg-blue-300 disabled:cursor-not-allowed text-white rounded-lg py-3 text-lg font-semibold transition flex items-center justify-center gap-2">
                        <span v-if="loading">
                            <LoaderCircle class="animate-spin" :size="26" />
                        </span>
                        <span v-else>Analisar</span>
                    </button>
                    <div v-if="resultado" class="mt-4 rounded-lg bg-blue-50 p-4 text-blue-800 font-medium shadow">
                        <span>{{ resultado }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { LoaderCircle, ScrollText } from "lucide-vue-next";
import axios from "axios";
export default {
    components: { LoaderCircle, ScrollText },
    data() {
        return {
            contrato: "",
            resultado: "",
            loading: false,
        };
    },
    methods: {
        async analisarContrato() {
            if (!this.contrato.trim()) return;
            this.resultado = "";
            this.loading = true;
            try {
                const res = await axios.post("http://127.0.0.1:5000/api/analisar", { texto: this.contrato });
                this.resultado = res.data.resultado;
            } catch (err) {
                this.resultado = "Erro ao conectar com o servidor.";
            }
            this.loading = false;
        },
    },
};
</script>
