        <template>
        <div class="container">
  <h1 class="headline"><strong>아기 정보</strong></h1>
  <br>
             <v-img
             src="../images/baby.png"
             height="200"
             width="200"
             class="mt-5"
             style="float:left;"
           >
           </v-img>
            <div style="float:right;">
               <v-col cols="12" style="left:25%">
               <span style="font-size: 1.5em" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="아기 이름" v-model="babyname">
              </v-col>
                <v-row>
    <v-col
      cols="12"
    >
      <v-menu
        ref="nowMenu"
        v-model="nowMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        :return-value.sync="birthday"
        transition="scale-transition"
        min-width="290px"
        offset-y
        full-width
      >
        <template v-slot:activator="{ on }">
            <v-col cols="12" style="left:25%">
            <span class="icon"><i class="fas fa-calendar-week" style="font-size: 1.5em"></i></span>
                <input v-model="birthday" v-on="on" type="text" placeholder="아기 생년월일" readonly >
            </v-col>
        </template>
        <v-date-picker
          v-model="birthday"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="nowMenu = false"
          >
            취소
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.nowMenu.save(birthday)"
          >
            선택
          </v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
  </v-row>
                 <v-col cols="12" style="left:25%">
               <span style="font-size: 1.5em; margin-top:-1px;" class="icon"><i class="far fa-id-card"></i></span>
                <input type="text" placeholder="배우자 이름" v-model="spousename">
               <button class="register" @click="babyinfo">가입하기</button>
</v-col>

        </div>
        </div>
</template>

<script>
import axios from 'axios';
import Calendar from './Calendar'
import {mapState} from 'vuex'
  export default {
    components:{Calendar},
   data: () => ({
      babyname: null,
      spousename: null,
      nowMenu: false,
      birthday: null,
    }),
     computed: {
        ...mapState({
    signupInfo: state=>state.moduleName.signupInfo
    })
    },
    methods: {
      babyinfo(){
  var vm;
  vm = `http://127.0.0.1:8000/account/${this.signupInfo.nickname}/babies/`;
  axios.post(vm,
  {
            "name": this.babyname,
            "birthday": this.birthday,
            "spouse": this.spousename,
        })
  .then(res => {
                        Swal.fire({
                  type: 'success',
                  text: '회원가입이 완료되었습니다',
        })
        .then(res=> this.$router.push('/login'))
                    })
                    .catch(err => {
                        alert('회원가입 실패');
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

.register {
  background-color: #F8BBD0;
  color: white;
  padding: 12px 20px;
  margin: 20px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

.register:focus{
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

</style>