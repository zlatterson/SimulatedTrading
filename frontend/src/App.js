
import './App.css';
import Dashboard from './containers/Dashboard';
import UserContainer from './containers/UserContainer';
import NavBar from './containers/NavBar';

import 'bootstrap/dist/css/bootstrap.min.css';
import Banner from './containers/Banner';
import Users from './containers/Users';


function App() {

  return (
<div className="App">
  <NavBar/>
  <Banner/>
  <Users/>
  <Dashboard/>
</div>
  );
}

export default App;
