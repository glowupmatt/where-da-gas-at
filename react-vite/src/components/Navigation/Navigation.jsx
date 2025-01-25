import { useContext } from "react";
import { GoogleMapContext } from "../../context/GoogleMapContext";
import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  const { openSideMenu } = useContext(GoogleMapContext);


  if (!openSideMenu) {
    return (
      <ul className={`nav-data-container-light`}>
        <li>
          <NavLink to="/" className={`logo-container-light`}>
            <img src="/gasIcon.svg" className="logo" alt="logo" />
            <p>Where da gas at?</p>
          </NavLink>
        </li>
        {/* <li>
          <DarkLightMode theme={theme} toggleTheme={toggleTheme} />
        </li> */}
        <li>
          <ProfileButton location="navigation-header" />
        </li>
      </ul>
    );
  }
  return <></>;
}

export default Navigation;
