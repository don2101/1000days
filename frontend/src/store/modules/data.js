// 다이어리, 계정정보 등 일반 데이터와 관련된 데이터스토어
// local storage에 저장

export default {
    namespaced: true,
    state: {
        isFollowModal: false,
        isAccSettingModal: false,
        isListView: true,
        showLeftSidebar: true,
        accountInfo: {'username': '영웅단비아빠'},
        diaryDataSet: {},
        searchedResult: {},
        loginedUserInfo: {'username': '아따맘마'},
        DetailModal: {'data': false},
    },
    getters: {
        isFollowModal: state => { return state.isFollowModal },
        DetailModal: state => { return state.DetailModal },
        isAccSettingModal: state => { return state.isAccSettingModal },
        isListView: state => { return state.isListView },
        accountInfo: state => { return state.accountInfo },
        diaryDataSet: state => { return state.diaryDataSet },
        searchedeRsult: state => { return state.searchedResult },
        loginedUserInfo: state => { return state.loginedUserInfo },
        showLeftSidebar: state => { return state.showLeftSidebar}
    },
    actions: {
        async initStore({state, commit}, accInfo, diary) {
            if (!state.accountInfo && !state.diaryDataSet) {
                commit('SET_INFOS_INIT', accInfo, diary);
            }
        },
        toggleViewType({commit}, bool) {
            commit('TOGGLE_VIEW_TYPE', bool);
        },
        toggleFM({commit}, bool) {
            commit('TOGGLE_FM', bool)
        },
        toggleLB({commit}, bool) {
            commit('TOGGLE_LB', bool)
        },
        setSerchedResult({commit}, resultData) {
            commit('SET_SEARCHED_RESULT', resultData);
        },
        setLoginedUserInfo({commit}, payload) {
            commit('SET_LOGINED_USER_INFO', payload)
        },
        setDetailModal({commit}, detailInfo) {
            commit('SET_DETAIL_MODAL', detailInfo)
        }

    },
    mutations: {
        SET_INFOS_INIT(state, accInfo, diary) {
            state.accountInfo = accInfo;
            state.diaryDataSet = diary;
        },
        TOGGLE_VIEW_TYPE(state, bool) {
            state.isListView = bool;
        },
        TOGGLE_FM(state, bool) {
            state.isFollowModal = bool;
        },
        TOGGLE_LB(state, bool) {
            state.showLeftSidebar = bool;
        },
        SET_SEARCHED_RESULT(state, resultData) {
            state.searchedResult = resultData;
        },
        SET_LOGINED_USER_INFO(state, payload) {
            state.loginedUserInfo = payload;
        },
        SET_DETAIL_MODAL(state, detailInfo) {
            state.DetailModal = detailInfo;
        }
    }


}