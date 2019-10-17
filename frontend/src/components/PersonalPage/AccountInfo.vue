<template>
    <div class="text-center" style="margin-bottom: 20px;">
        <div>
            <!--follower: n명 / following: m명-->
            <v-btn large text color="primary">Following: n명</v-btn> <v-btn large text color="primary">Follower: m명</v-btn>
        </div>
        <div>
            <!--검색(게시글 제목 또는 내용으로) / 달력형 뷰(아이콘) / 계정정보 수정(계정 주인한테만 보이기)-->
            <div v-if="isSearch" style="width: 200px; display: inline-block" class="search-form slide-left">
                <v-text-field v-model="diarySearch" placeholder="제목 또는 내용 검색"></v-text-field>
            </div>
            <img class="c-pointer icons" width="20px" height="20px" src="https://img.icons8.com/wired/50/000000/search.png" alt="search-icon" @click="isSearch = !isSearch">
            <!--리스트형 보기-->
            <img class="c-pointer icons" width="20px" height="20px" src="https://img.icons8.com/ios/50/000000/overview-pages-3.png" alt="list-icon">
            <!-- 캘린더형 보기-->
            <img class="c-pointer icons" width="20px" height="20px" src="https://img.icons8.com/wired/50/000000/calendar.png" alt="calender-icon">
            <img class="c-pointer icons" width="20px" height="20px" src="https://img.icons8.com/ios-filled/50/000000/gear.png" alt="setting-icon">
        </div>
        <div>
           <!--글 작성하기(계정 주인한테만 보이기)-->
        </div>
        <AccountSettingModal/>

    </div>

</template>


<script>
  import AccountSettingModal from "./AccountSettingModal";
  export default {
      components: {AccountSettingModal},
      data () {
        return {
            diarySearch: '',
            isSearch: false,

        }
    }
  }
</script>

<style>
    @keyframes slide-left {
      0% {
        -webkit-transform: translateX(50px);
                transform: translateX(50px);
      }
      100% {
        -webkit-transform: translateX(0px);
                transform: translateX(0px);
      }
    }

    .text-center {
        text-align: center;
    }
    .c-pointer {
        cursor: pointer;
    }
    .icons {
        margin: 10px 0 0 15px;
    }
    .slide-left {
        -webkit-animation: slide-left 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
        animation: slide-left 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
</style>