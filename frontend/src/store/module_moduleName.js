const initialState={
    signupInfo: null,
    userInfo: null,
}

const mutations= {
     setNicknameInfo(state, info) {
        state.signupInfo = info
      },
      setUserInfo(state,info){
        state.userInfo = info
      }
  }

  export default{
    state: {
        ...initialState
    },
    mutations,
}
