<template>
<div class="container">
<v-card class="mx-auto"
    max-width="600"
      height="200"
    >
    <h1>비밀번호를 입력해주세요</h1>
     <v-col cols="12">
  <v-text-field
    v-model="repassword"
    :type="show ? 'text' : 'password'"
    name="input-10-1"
    label="password"
    hint="10자 이상 입력하세요">
    </v-text-field>
    </v-col>
    <v-btn color="primary" class="mr-3" style="float:right" @click="enter">확인</v-btn>
    </v-card>
    </div>
</template>


<script>
export default {
  name: 'AccountPage',
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
<style>
  .container {
      width: 70%;
}
</style>