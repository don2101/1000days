<template>
    <v-container class="grey lighten-5">
        <v-row no-gutters>
          <v-col cols="4" sm="4" style="margin-top: 20px;">
          <div class="text-center" style="margin-bottom: 15px">
            <v-avatar>
                <img
                src="https://cdn.vuetifyjs.com/images/john.jpg"
                alt="John"
                >
            </v-avatar>
          <span style="display:inline-block; margin-left: 15px">{{accountInfo.username}}</span>

          </div>
            <div v-if="loginedUserInfo.username!==accountInfo.username">
                <v-btn block color="blue" style="color: white;" @click="commitFollow()">Follow</v-btn>
            </div>
            <div class="text-center" v-else>
                <div class="c-pointer">
                    <img class="c-pointer icons" width="20px" height="20px"
                         title="계정 설정"
                         v-if="loginedUserInfo.username===accountInfo.username"
                         src="https://img.icons8.com/dusk/64/000000/admin-settings-male.png">&nbsp
                    <small>계정 설정</small>
                </div>
                <!-- 글쓰기 -->
                <div class="c-pointer" @click="$router.push('/mydiary/new')">
                    <img class="icons" width="20px" height="20px"
                         title="새 글 작성"
                         v-if="loginedUserInfo.username===accountInfo.username"
                         src="https://img.icons8.com/dusk/64/000000/book-and-pencil.png"
                        >&nbsp
                    <small>글쓰기</small>
                </div>
            </div>
          </v-col>
          <v-col cols="12" sm="8" class="text-center">
            <div>
                <span style="display: inline-block; margin: 20px; font-family: 'Nanum Myeongjo', serif;">
                    계정소개 계정소개 계정소개 계정소개 계정소개 계정소개 계정소개 계정소개 계정소개 계정소개
                </span>
                <div>
                    <v-btn large text color="primary" @click="toggleFM(true)">Following: n명</v-btn> <v-btn large text color="primary" @click="toggleFM(true)">Follower: m명</v-btn>
                </div>
                <div>
                    <!--검색(게시글 제목 또는 내용으로) / 달력형 뷰(아이콘) / 계정정보 수정(계정 주인한테만 보이기)-->
                    <div v-if="isSearch" style="width: 200px; display: inline-block" class="search-form slide-left">
                        <v-text-field v-model="diarySearch" placeholder="제목 또는 내용 검색"></v-text-field>
                    </div>
                    <img class="c-pointer icons" width="20px" height="20px"
                         title="게시물 검색하기"
                         src="https://img.icons8.com/wired/50/000000/search.png" alt="search-icon" @click="isSearch = !isSearch">
                    <!--리스트형 보기-->
                    <img class="c-pointer icons" width="20px" height="20px"
                         title="리스트로 보기"
                         src="https://img.icons8.com/ios/50/000000/overview-pages-3.png" alt="list-icon" @click="toggleViewType(true)">
                    <!-- 캘린더형 보기-->
                    <img class="c-pointer icons" width="20px" height="20px"
                         title="달력으로 보기"
                         src="https://img.icons8.com/wired/50/000000/calendar.png" alt="calender-icon" @click="toggleViewType(false)">
<!--                    &lt;!&ndash; 계정 설정&ndash;&gt;-->
<!--                    <img class="c-pointer icons" width="20px" height="20px"-->
<!--                         title="계정 설정"-->
<!--                         v-if="loginedUserInfo.username===accountInfo.username"-->
<!--                         src="https://img.icons8.com/dusk/64/000000/admin-settings-male.png">-->
<!--                    &lt;!&ndash; 글쓰기 &ndash;&gt;-->
<!--                    <img class="c-pointer icons" width="20px" height="20px"-->
<!--                         title="새 글 작성"-->
<!--                         v-if="loginedUserInfo.username===accountInfo.username"-->
<!--                         src="https://img.icons8.com/dusk/64/000000/book-and-pencil.png"-->
<!--                        @click="$router.push('/mydiary/new')">-->
                </div>

            </div>
          </v-col>
        </v-row>
      </v-container>

</template>


<script>
    import {mapActions, mapGetters} from 'vuex'
  import AccountSettingModal from "./AccountSettingModal";
  export default {
      components: {AccountSettingModal},
      data () {
        return {
            diarySearch: '',
            isSearch: false,

        }
    },
      methods: {
          ...mapActions('data', ['toggleViewType', 'toggleFM']),
          commitFollow() {
                Swal.fire({
                type: 'success',
                text: 'Following 목록에 추가되었습니다.',
            })
          }
      },
      computed: {
          ...mapGetters('data', ['accountInfo', 'loginedUserInfo'])
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