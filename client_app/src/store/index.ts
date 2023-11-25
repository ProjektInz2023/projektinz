import { createStore } from 'vuex'

export default createStore({
  state: {
    userid: 0 as number,
    response: Object,
    Orders: [
    ],
    User: [

    ]
  },
  getters: {
    currentUser: (state) => state.userid
  },
  mutations: {
    logout_session (state) {
      state.userid = 0
    },
    register_session (state, id) {
      state.userid = id
    },
    insert_orders (state, payload) {
      state.Orders = payload
    },
    insert_user (state, payload) {
      state.User = payload
    }
  },
  actions: {
    logoutSession ({ commit }) {
      commit('logout_session')
    },
    registerSession ({ commit }) {
      commit('register_session')
    },
    insertOrders ({ commit }, data) {
      commit('insert_orders', data)
    },
    insertUser ({ commit }, data) {
      commit('insert_user', data)
    }
  },
  modules: {
  }
})
