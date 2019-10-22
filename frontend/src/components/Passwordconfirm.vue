<template>
<div class="container">
<v-card class="mx-auto"
    max-width="600"
      height="220"
    >
<div class="title">
    <h1>비밀번호를 입력해주세요</h1>
    </div>
    <v-card-text>
   <v-col cols="12">
     <span class="icon"><v-icon>fas fa-lock</v-icon></span>
     <input type="password" placeholder="비밀번호" v-model="repassword" required>
    </v-col>
    <v-card-actions>
       <v-spacer></v-spacer>
    <v-btn color="pink" class="mr-3" @click="enter">확인</v-btn>
    </v-card-actions>
     </v-card-text>
    </v-card>
    </div>
</template>


<script>
export default {
   data: () => ({
      repassword: null,
      show: false,
    }),
  components: {
  },
  computed:{
     checkpw() {
            if(this.repassword==null || this.repassword!=1234) return false
            return true
        },
  },
  methods: {
    enter(){
    if (this.repassword==null || this.repassword!=1234){
        Swal.fire({
                  type: 'error',
                  text: '비밀번호가 틀렸습니다. 다시 입력해주세요',
        })
    }
   if (this.repassword==1234){
    this.goToMyPage()
  }
  },
      goToMyPage(){
    this.$router.push({
        name: 'AccountPage'
    })
  }
  }
  }
</script>
<style scoped>
  .container {
      width: 70%;
}

h1{
color:#F8BBD0;
text-align: center;
}

input{
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  box-sizing: border-box;
  background-color: #EEEEEE;
  padding-left: 50px;
  transition: 1s;
}

input:focus{
outline: none;
border-color:#F8BBD0;
box-shadow: 0 0 8px 0 #F8BBD0;
}

input::placeholder {
  font-weight: bold;
}

.icon{
  position: absolute;
  top: 15%;
  margin-left: 17px;
  margin-top: 17px;
  z-index: 1;
  color: #4f5b66;
}

.mr-3{
color:#fff;
}
</style>