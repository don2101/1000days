<template>
    <v-app-bar
      app clipped-left
      color="#FDEDEC" style="height: 70px; margin: auto;"
    >
      <!--로고와 사이트 이름-->
      <img style="margin-top: 15px" width="43px" height="43px" src="https://img.icons8.com/nolan/64/000000/baby-feet.png">
      <!-- <img style="margin-top: 15px" src="../../public/favicon.png"> -->
      <span @click="$router.push('/')" class="ml-3 mr-5 site-title">1000 Days&nbsp;</span>

      <!-- 다른 계정 검색창 -->
      <v-text-field
          placeholder="Search"
          single-line
          color="white"
          hide-details
          v-model=searchText
          style="margin-left: 12%"
        ></v-text-field><img class="c-pointer" width="20px" height="20px" src="https://img.icons8.com/wired/50/000000/search.png">
      <v-spacer></v-spacer>

      <span class="username">{{loginedUserInfo.username}}</span>
      <!-- 상단 메뉴 -->
      <div class="text-center">
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-avatar color="#99A3A4" v-on="on" class="c-pointer">
              <v-icon dark>mdi-account-circle</v-icon>
            </v-avatar>
          </template>

          <v-list dense>
            <v-list-item-group v-model="item" color="primary">
              <v-list-item
                v-for="i in menus.length"
                :key="i"
              >
                <v-list-item-title class="c-pointer" @click="$router.push(actions[i-1])">
                  <i :class="icons[i-1]" :style="iconColors[i-1]"></i>&nbsp {{ menus[i-1] }}
                </v-list-item-title>

              </v-list-item>
            </v-list-item-group>
          </v-list>

        </v-menu>
      </div>


    </v-app-bar>
</template>

<script>
  import {mapGetters} from 'vuex'
    export default {
      name: "Header",
      data() {
        return {
          searchText: '',
          menus: ['  home','  my page','  my diary','  logout',],
          icons: ['fas fa-home', 'far fa-user-circle','fas fa-book','fas fa-sign-out-alt'],
          iconColors: ['color: black', 'color: #f0d2d1', 'color: #e6f792', 'color: #a70d56'],
          actions: ["/", "/login","/test/mydiary","/signup"],
          searchResult: ['dfd', 'dfd', 'sdfadf', 'asdfadfl;kj'],
        }
      },
      watch: {
        searchText() {
          console.log(this.searchText)
        }
      },
      computed: {
        ...mapGetters('data', ['loginedUserInfo'])
      },
      mounted() {
      },
  }
</script>

<style>
    .site-title {
        font-family: 'Plaster', cursive;
        font-size: 25px;
        cursor: pointer;
    }

    .c-pointer {
      cursor: pointer;
    }
  .username {
    margin-right: 5px
  }
</style>