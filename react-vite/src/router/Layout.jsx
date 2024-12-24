import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";
import { GoogleMapProvider } from "../context/GoogleMapContext";

export default function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    try {
      dispatch(thunkAuthenticate());
      setIsLoaded(true);
    } catch (e) {
      console.error(e);
    }
  }, [dispatch]);

  return (
    <>
      <GoogleMapProvider>
        <ModalProvider>
          <Navigation />
          {isLoaded && <Outlet />}
          <Modal />
        </ModalProvider>
      </GoogleMapProvider>
    </>
  );
}
