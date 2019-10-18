<template>
<div>
<v-container>
<v-card>
<div class="title">
<h2 style="color: #B0BEC5; text-align: center;">탈퇴 안내</h2>
<p class="sub">회원탈퇴를 신청하기 전에 안내 사항을 꼭 확인해주세요.</p>
</div>
<v-card-text>
<div class="text1">
<h5>사용하고 계신 아이디는 탈퇴할 경우 재사용 및 복구가 불가능합니다.</h5>
탈퇴한 아이디는 본인과 타인 모두 재사용 및 복구가 불가하오니 신중하게 선택하시기 바랍니다.<br>
</div>
<div class="text2">
<h5>탈퇴 후 회원정보는 모두 삭제됩니다</h5>
회원정보는 모두 삭제되며, 삭제된 데이터는 복구되지 않습니다.</br>
삭제되는 내용을 확인하시고 필요한 데이터는 미리 백업을 해주세요<br>
</div>
<div class="text3">
<h5>탈퇴 후 게시판형 서비스에 등록한 게시물은 모두 삭제됩니다</h5>
육아일기 등에 올린 게시글 및 댓글은 탈퇴 시 자동 삭제됩니다<br>
탈퇴 후에는 아이디로 다시 가입할 수 없으며 아이디와 데이터는 복구할 수 없습니다.<br>
게시판형 서비스에 남아 있는 게시글은 탈퇴 후 자동 삭제됩니다.
</div>

 <v-row align="center">
        <v-checkbox
          v-model="checkbox"
          hide-details
          class="shrink mr-2 mt-5"
        ></v-checkbox>
        <p class="mt-10">안내 사항을 모두 확인하였으며, 이에 동의합니다.</p>
      </v-row>

      <v-card-actions>
<v-btn style="left:90%;" color="pink lighten-2" @click="withdrawal()"><i class="fas fa-sign-out-alt"></i><small style="font-weight: bold;color:#fff">탈퇴</small></v-btn>
</v-card-actions>
</v-card-text>
</v-card>
</v-container>
</div>
</template>
<script>
export default {
 data: () => ({
      checkbox: false,
    }),
  methods: {
   withdrawal(){
     Swal.fire({
  title: '정말 탈퇴하시겠습니까?',
  text: "탈퇴취소는 불가능합니다",
  type: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: '탈퇴하기',
  cancelButtonText: '취소'
}).then((result) => {
  if (result.value) {
    this.$router.push({
        name: 'HomePage'
    })
  }
})
    },
    }
  }
</script>

<style scoped>

h1{
color:#F8BBD0;
text-align: center;
}
.text1, .text2, .text3{
margin-top:50px;
}

.sub{
text-align: center;
}

.title{
margin-top: 100px;
}

h5{
color:red;
}

.fa-sign-out-alt{
color:#fff;
}
</style>