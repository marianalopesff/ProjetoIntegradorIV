<template>
  <header class="bg-white shadow-md fixed top-0 left-0 w-full z-50 h-24 flex items-center justify-center">
    <nav class="flex space-x-8 font-semibold text-gray-600 font-montserrat">
      <router-link to="/" class="group relative transition-colors duration-200 px-4 py-2"
        :class="$route.path === '/' ? 'text-blue-600 font-bold' : ''">
        ANALISADOR DE CONTRATOS
        <span class="absolute left-0 bottom-0 h-0.5 transition-all duration-300"
          :class="$route.path === '/' ? 'w-full bg-blue-600 group-hover:bg-blue-800' : 'w-0 bg-blue-800 group-hover:w-full'">
        </span>
      </router-link>
      <router-link to="/aba2" class="group relative transition-colors duration-200 px-4 py-2"
        :class="$route.path === '/aba2' ? 'text-blue-600 font-bold' : ''">
        DETALHES  
        <span class="absolute left-0 bottom-0 h-0.5 transition-all duration-300"
          :class="$route.path === '/aba2' ? 'w-full bg-blue-600 group-hover:bg-blue-800' : 'w-0 bg-blue-800 group-hover:w-full'">
        </span>
      </router-link>

    </nav>
  </header>
</template>

<script setup>
// Não há mais lógica JS necessária, tudo é feito via Vue Router!
</script>

<style scoped>
header {
  min-width: 100vw;
}

nav {
  position: relative;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.group {
  position: relative;
  cursor: pointer;
  transition: color 0.3s;
}

.group:hover {
  color: #1e40af;
  /* Azul escuro */
}

.group span {
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  border-radius: 2px;
}

.group:hover span {
  transition: width 0.3s, background 0.3s;
}

@media (max-width: 768px) {
  header {
    height: 64px;
  }

  nav {
    font-size: 1rem;
  }
}
</style>
