<template>
<div>
<div class="container">
<v-card class="mx-auto"
    max-width="600"
      height="350"
    >
    <h1>LOGIN</h1>
     <v-col cols="12">
    <v-text-field
      v-model="email"
      label="E-mail">
    </v-text-field>
    </v-col>
    <v-col cols="12">
  <v-text-field
    v-model="password"
    :type="show1 ? 'text' : 'password'"
    name="input-10-1"
    label="password"
    hint="10자 이상 입력하세요">
    </v-text-field>
    </v-col>
    <v-btn color="primary" style="left:55%;" @click="login">로그인</v-btn>
    <Signup></Signup>
    </v-card>
    </div>
    </div>
</template>

<script>
import Signup from './Signup'
  export default {
    data: () => ({
      email: null,
      password: null,
      show1: false,
    }),
    components:{
    Signup
    },
    computed: {
    isFill() {
            if(this.email===null || this.email.trim()=== '' || this.password === null || this.password.trim() === '') return false
            return true
        },
    },

    methods: {
      login () {
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
       else {Swal.fire({
          type: 'success',
          text: 'Welcome!',
        })
      }
}
    },
  }
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