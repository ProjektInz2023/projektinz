import { createStore } from 'vuex'

export default createStore({
  state: {
    userid: 0 as number,
    response: Object,
    Orders: [
      {
        id: 0 as number,
        title: 'title1' as string,
        description: 'desc2' as string
      },
      {
        id: 1 as number,
        title: 'title2'as string,
        description: 'desc2' as string
      }
    ]
  },
  getters: {
    currentUser: (state) => state.userid,
    currentOrders: (state) => state.Orders
  },
  mutations: {
    logout_session (state) {
      state.userid = 0
    },
    register_session (state, id) {
      state.userid = id
    }
  },
  actions: {
    logoutSession ({ commit }) {
      commit('logout_session')
    },
    registerSession ({ commit }) {
      commit('register_session')
    }
  },
  modules: {
  }
})
