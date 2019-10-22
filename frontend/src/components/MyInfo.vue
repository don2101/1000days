<template>
<div class="container">
<div class="row">
  <div class="col-3">
    <h1>My Page</h1>
    <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link" id="v-pills-home-tab" data-toggle="pill" @click="editinfo()" role="tab" aria-selected="false">회원정보</a>
      <a class="nav-link active" id="v-pills-profile-tab" data-toggle="pill" @click="remove()" role="tab" aria-selected="true">회원탈퇴</a>
    </div>
  </div>
</div>
<div v-if="show==true">
<EditInfo></EditInfo>
</div>
<div  v-if="show==false">
<Withdrawal></Withdrawal>
</div>
</div>
</template>


<script>
import Withdrawal from './Withdrawal'
import EditInfo from './EditInfo'
export default {
  name: 'AccountPage',
     data: () => ({
      show: false,
      }),
   components: {
    Withdrawal,
    EditInfo
  },
  methods: {
    remove(){
        this.show = false
    },
    editinfo(){
        this.show = true
    },
  },
  }
</script>

<style scoped>
.container{
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

.material-icons{
color:#fff;
}

</style>