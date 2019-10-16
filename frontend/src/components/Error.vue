<template>
<div>
<div class="container">
<v-card class="mx-auto"
    max-width="500"
      height="300"
    >
    <h1>ERROR</h1>
    <v-card-text>
    <h4 style="text-align: center;">
    로그인 한 회원만<br> 들어올 수 있는 페이지입니다.<br>
    로그인을 해주세요!<hr>
    로그인 하러 가기
    </h4>
    <v-btn color="primary" class="mr-3" style="left:40%" @click="$router.push('/')">click</v-btn>
    </v-card-text>
    </v-card>
    </div>
    </div>
</template>

<script>
  export default {
    components:{},
    methods: {},
  }
</script>

<style>
  .container {
      width: 70%;
}

h1{
color:#1E88E5;
text-align: center;
}
</style>