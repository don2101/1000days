<template>
    <v-app-bar
      app clipped-left
      color="#FDEDEC" style="height: 70px; margin: auto;"
    >
      <!--로고와 사이트 이름-->
      <img style="margin-top: 15px" src="https://img.icons8.com/nolan/64/000000/baby-feet.png">
      <!-- <img style="margin-top: 15px" src="../../public/favicon.png"> -->
      <span @click="$router.push('/')" class="ml-3 mr-5 site-title">1000 Days&nbsp;</span>
      
      <!-- 검색창 -->
      <v-text-field
          placeholder="Search"
          single-line
          color="white"
          hide-details
          :value=searchText
          style="margin-left: 16%"
        ></v-text-field><img class="c-pointer" width="20px" height="20px" src="https://img.icons8.com/wired/50/000000/search.png">
      <v-spacer></v-spacer>


      <!-- 상단 메뉴 -->
      <div class="text-center">
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-avatar color="#99A3A4" v-on="on" class="c-pointer">
              <v-icon dark>mdi-account-circle</v-icon>
            </v-avatar>
          </template>
          <v-list>
            <v-list-item
              v-for="menu in menus"
              :key="menu"
            >
              <v-list-item-title>{{ menu }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>

      
    </v-app-bar>
</template>

<script>
    export default {
      name: "Header",
      data() {
        return {
          searchText: '',
          menus: ['home', 'logout','account', 'diary'],
          searchResult: ['dfd', 'dfd', 'sdfadf', 'asdfadfl;kj'],
        }
      },
      watch:{
        searchText() {
          console.log(this.searchText);
        }
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
</style>