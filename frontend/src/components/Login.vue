<template>
<div>
<v-card class="mx-auto"
    max-width="300"
    height="350"
    >
    <h1>LOGIN</h1>
    <v-col cols="12">
    <span class="icon"><i style="font-size:1.5rem" class="fad fa-envelope"></i></span>
     <input type="text" placeholder="이메일" v-model="email" required>
    </v-col>
    <v-col cols="12">
     <span class="icon"><i class="fad fa-lock" style="font-size:1.5rem"></i></span>
     <input type="password" placeholder="비밀번호" v-model="password" required>
    </v-col>
    <button class="mr-3" style="float:right" @click="login()"> <i class="fad fa-sign-in-alt" style="font-size:1.5rem"></i>로그인</button>
    </v-card>
    </div>
</template>

<script>
import axios from 'axios';
import {mapState, mapGetters, mapActions} from 'vuex';
  export default {
    data: () => ({
      email: null,
      password: null,
    }),
    components:{
    },
    computed: {
    enterkey() {
        if (window.event.keyCode == 13) {

             // 엔터키가 눌렸을 때 실행할 내용
             login();
        }
},
    ...mapGetters(
        'auth', ['userInfo']
    ),
    isFill() {
            if(this.email===null || this.email.trim()=== '' || this.password === null || this.password.trim() === '') return false
            return true
        },
    },

    methods: {
    ...mapActions('auth', ['saveuserInfo']),
      login (email,password) {
        if(!this.isFill){
             Swal.fire({
                  type: 'error',
                  text: '이메일 또는 비밀번호를 입력해주세요',
        })
      }
      if (this.isFill){
        if (this.password.length>0&&this.password.length<10){
            Swal.fire({
                  type: 'error',
                  text: '비밀번호를 10자 이상 입력해주세요',
        })
      }
     else {
      axios.post('http://localhost:8000/account/login/', {'email': this.email, 'password': this.password})
       .then(res=>sessionStorage.setItem("token",res.data.token))
       .then(res=>this.saveuserInfo(this.email))
       .then(res=>{
                          Swal.fire({
                 type: 'success',
                 text: '로그인 되었습니다',
       })
       })
       .then(res=> this.$router.push('/'))
        .catch(err => {
                       Swal.fire({
                 type: 'error',
                 text: '로그인 실패',
       })
                   })
   }
    }
    },
    goToMain(){
    this.$router.push({
        name: 'HomePage'
    })
  }
  },
  }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Chewy|Jua&display=swap');
h1{
    color:#F8BBD0;
    text-align: center;
    font-family: 'Chewy', cursive;
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

button {
  background-color: #F8BBD0;
  color: white;
  padding: 12px 20px;
  margin: 20px 0;
  border: none;
  cursor: pointer;
  width: 90%;
}

button:focus{
outline: none;
}

.icon{
  position: absolute;
  top: 15%;
  margin-left: 17px;
  margin-top: 17px;
  z-index: 1;
  color: #4f5b66;
  transition: 1s;
}

.icon input:focus +i{
color: #F8BBD0;
}

.fa-sign-in-alt{
    margin-right:10px;
}

.mr-3{
font-family: 'Jua', sans-serif;
}
</style>                  