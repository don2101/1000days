const initialState={
    userInfo: 'null',
}

const mutations= {
     setUserInfo(state, info) {
        state.userInfo = info
      },
  }

  export default{
    state: {
        ...initialState
    },
    mutations,
}
