import { createRouter, createWebHistory } from 'vue-router'
import Aba1View from '../views/Aba1View.vue'
import Aba2View from '../views/Aba2View.vue'
import Aba3View from '../views/Aba3View.vue'


const routes = [
  { path: '/', name: 'Aba1', component: Aba1View },
  { path: '/aba2', name: 'Aba2', component: Aba2View },
  { path: '/aba3', name: 'Aba3', component: Aba3View }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    // Se tem hash (ex: #produtos), scrolla depois do DOM montar
    if (to.hash) {
      return new Promise((resolve) => {
        // aguarda o próximo ciclo do DOM/render
        setTimeout(() => {
          resolve({
            el: to.hash,
            behavior: 'smooth',
          })
        }, 100) // 300ms é seguro, pode ajustar
      })
    }

    // Se volta para cima, ou muda de página sem hash
    return { top: 0 }
  }
  ,
})

export default router
