<template>
<div>
<div class="container">
<v-card class="mr-3">
<v-layout wrap>
        <v-flex xs12 sm6>
     <v-img
             src="../images/family.png"
             height="200"
             width="200"
             class="mt-5 ml-5"
           ></v-img>
           </v-flex>
             <v-flex xs12 sm6>
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
      <h6>로그인 하러 가기</h6>
      <v-btn color="pink" class="ml-3 mr-3" @click="$router.push('/login')"><i class="fas fa-hand-pointer"></i>&nbsp;click</v-btn>
    </v-card-actions>
    </v-card-text>
    </v-flex>
    </v-layout>
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
font-family: 'Chewy', cursive;
}

h4, h5, h6{
color:grey;
font-family: 'Jua', sans-serif;
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