<template>
<div>
<div class="container">
<v-card>
     <v-img
             src="../images/family.png"
             height="200"
             width="200"
             class="mr-5"
             style="float:left;"
           ></v-img>
    <v-card-text>
      <h1>ERROR</h1>
    <h4 class="mt-5 mb-10">
    접근 권한이 없는 페이지
    </h4>
    <h5 class="mt-5 mb-10">
     MyPage는 회원전용 페이지입니다
    </h5>
    <v-card-actions>
      <v-spacer></v-spacer>
      로그인 하러 가기
    <v-btn color="pink" class="ml-3 mr-3" @click="$router.push('/login')"><i class="fas fa-hand-pointer"></i>&nbsp;click</v-btn>
    </v-card-actions>
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

<style scoped>
  .container {
      width:70%;
}

h1{
color:red;
}

h4{
margin-left:75px;
font-weight: bold;
}

.text{
margin-top:100px;
}

v-btn{
color:white;
}

.mr-3{
color:#fff;
}
</style>