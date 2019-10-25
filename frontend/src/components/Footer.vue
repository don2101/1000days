<template>
    <v-footer
      absolute
      app
      color="#EBEDEF"
      class="white--text"
    >
      <div style="color: gray; "><a href="https://lab.ssafy.com/s1-final/s1p1351023" target="blank">SSAFY 23팀</a><br>
      <a href="mailto: lar404@naver.com">Lee Ahrum</a> / 
      <a href="mailto: lar404@naver.com">Yeom Heedon</a> / 
      <a href="mailto: lar404@naver.com">Shim Ieeju</a> / 
      <a href="mailto: lar404@naver.com">Hwang Youseong</a></div>
      <v-spacer></v-spacer>
      <span style="color: gray">&copy; 2019</span>
    </v-footer>

</template>

<script>
    export default {
      name: "Footer",
      data() {
        return {

        }
      },

    }
</script>
<style>
  a:link {
    color: gray !important; text-decoration: none;
    }
  a:visited {
    color: gray !important; text-decoration: none;
    }
  a:hover {
    color: black !important; text-decoration: none;
    }

</style>