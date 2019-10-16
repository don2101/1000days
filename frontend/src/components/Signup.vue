<template>
<div>
     <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
    <template v-slot:activator="{ on }">
         <v-btn color="#FBC02D" class="ml-3" style="float:left;" v-on="on">회원가입</v-btn>
      </template>
        <v-card>
          <h1 class="headline"><strong>회원 정보</strong></h1>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-text-field
                  label="이름*"
                  v-model="name"
                  required
                ></v-text-field>
              </v-col>
               <v-col cols="12" sm="6">
                <v-text-field
                  label="닉네임*"
                  v-model="nickname"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="이메일*" v-model="newemail" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="비밀번호*" type="password" v-model="pw" required hint="10자 이상 입력해주세요"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="비밀번호 확인*" type="password" v-model="repw" required></v-text-field>
             <div v-if="this.pw!=this.repw">
              <p style="color:red;">비밀번호가 일치하지 않습니다</p>
              </div>
              </v-col>
              <v-radio-group v-model="babyYN" :mandatory="false">
              <h6>아기가 있습니까?</h6>
              <br>
              <v-radio label="있음" value="babyY"></v-radio>
              <v-radio label="없음" value="babyN"></v-radio>
            </v-radio-group>
            <div v-if="babyYN=='babyY'">
              <v-col cols="12">
                </v-col>
                <v-col cols="12" style="left:200%;">
                <v-text-field
                  label="아기 이름"
                  v-model="babyname"
                ></v-text-field>
              </v-col>
              <v-col cols="12" style="left:200%;" >
                <v-text-field
                  label="배우자 이름"
                  v-model="spousename"
                ></v-text-field>
              </v-col>
                  <Calendar></Calendar>
        </div>
            </v-row>
          </v-container>
       <v-radio-group v-model="accountYN" :mandatory="false">
              <h6>계정 공개 여부 설정*</h6>
              <br>
              <v-radio label="공개" value="accountY"></v-radio>
              <v-radio label="비공개" value="accountN"></v-radio>
            </v-radio-group>
        <v-radio-group v-model="followYN" :mandatory="false">
              <h6>팔로우/팔로잉 공개 여부 설정*</h6>
              <br>
              <v-radio label="공개" value="followY"></v-radio>
              <v-radio label="비공개" value="followN"></v-radio>
            </v-radio-group>
        </v-card-text>
        <br>
        <small><p style="text-align:center;">*필수입력항목</p></small>
        <small><p style="text-align:center;">*아직 아기가 태어나지 않은 경우 출산예정일을 입력해주세요 (태어난 후 아기생일로 수정해주세요)</p></small>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">취소하기</v-btn>
          <v-btn color="red" text @click="signup">가입하기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    </v-card>
    </div>
</template>

<script>
import Calendar from './Calendar'
  export default {
    data: () => ({
      dialog: false,
      name: null,
      nickname: null,
      newemail:null,
      pw: null,
      repw: null,
      babyYN: 'babyY',
      babyname: null,
      spousename: null,
      accountYN: 'accountY',
      followYN: 'followY'
    }),
    components:{
        Calendar
    },
    computed: {
     isValidate: function() {
      if (this.name === null || this.nickname === '' || this.newemail === null || this.pw === '' || this.repw === null)
        return false
      else return true
    }
    },

    methods: {
    signup(){
    if (!this.isValidate) {
         Swal.fire({
                  type: 'error',
                  text: '모든 항목을 입력해주세요',
        })
      }
    if (this.pw != this.repw || this.pw.length<10 ){
        alert('비밀번호를 확인해주세요')
    }
    else {
    alert('회원가입이 완료되었습니다')
    this.dialog = false
    }
  },
  }
  }
</script>

<style>

h1{
color:#1E88E5;
text-align: center;
}
</style>