<template>
  <header>
    <Navbar />
  </header>
  <main>
    <div class="search-container">
      <div class="search-box">
        <input type="text" name="stockname" placeholder="股票名稱">
        <button type="submit">搜尋</button>
      </div>
    </div>
  </main>
</template>

<script>
import Navbar from '../components/Navbar.vue';

export default {
  name: 'HomeView',
  components: {
    Navbar
  }
}
</script>

<style>
  .search-container{
    width: 80%;
    height: 60px;
    margin:30px auto;
    border: 1px solid gray;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: gray;
    border-radius: 10px;
  }
  .search-box{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap:1%
  }
  .search-box input{
    width: 80%;
    height: 40px;
    border: 1px solid black;
    border-radius: 10px;
  }
  .search-box button{
    width: 5%;
    height: 40px;
    border-radius: 10px;
  }
</style>