import React, { useState } from "react";
import { SkynetClient, genKeyPairFromSeed } from "skynet-js";
import SkynetSVG from "./assets/skynet.svg";

const skynetClient = new SkynetClient(process.env.REACT_APP_PORTAL_URL);
const filename = "data.json";

function App() {
  const [secret, setSecret] = useState("");
  const [transaction, setTransaction] = useState("");
  const [revision, setRevision] = useState(0);
  const [authenticated, setAuthenticated] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [displaySuccess, setDisplaySuccess] = useState(false);
  const handleReset = () => {
    setSecret("");
    setTransaction("");
    setRevision(0);
    setErrorMessage("");
    setLoading(false);
    setDisplaySuccess(false);
    setAuthenticated(false);
  };
  const loadTransaction = async () => {
    try {
      const { publicKey } = genKeyPairFromSeed(secret);
      const entry = await skynetClient.db.getJSON(publicKey, filename);

      if (entry) {
        setTransaction(entry.data?.transaction ?? "");
        setRevision(entry.revision);
      }
    } catch (error) {
      setErrorMessage(error.message);
      setTransaction("");
    }
  };
  const handleLogin = async (event) => {
    event.preventDefault();
    setLoading(true);

    await loadTransaction();

    setAuthenticated(true);
    setLoading(false);
  };
  const handleSetTransaction = async () => {
    setLoading(true);

    const { privateKey } = genKeyPairFromSeed(secret);
    try {
      await skynetClient.db.setJSON(
        privateKey,
        filename,
        { transaction },
        revision + 1
      );

      setRevision(revision + 1);
      setDisplaySuccess(true);
      setTimeout(() => setDisplaySuccess(false), 5000);
    } catch (error) {
      setErrorMessage(error.message);
    }

    setLoading(false);
  };

  return (
    <div>
    <div className="bg-background min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div className="flex flex-wrap py-2">
  <div className="w-full px-4">
    <nav className="relative flex flex-wrap items-center justify-between px-2 py-3 bg-emerald-500 rounded">
      <div className="container px-4 mx-auto flex flex-wrap items-center justify-between">
        <div className="w-full relative flex justify-between lg:w-auto px-4 lg:static lg:block lg:justify-start">
          <h2 className="text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-white">
            Cryptots Fund Menu
          </h2>
          <button className="cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none" type="button">
            <span className="block relative w-6 h-px rounded-sm bg-white"></span>
            <span className="block relative w-6 h-px rounded-sm bg-white mt-1"></span>
            <span className="block relative w-6 h-px rounded-sm bg-white mt-1"></span>
          </button>
        </div>
        <div className="flex lg:flex-grow items-center" id="example-navbar-info">
          <ul className="flex flex-col lg:flex-row list-none ml-auto">
            <li className="nav-item">
              <a className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75" href="index.html">
              Record new transactions and other important data(main page)
              </a>
            </li>
            <li className="nav-item">
              <a className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75" href="Vote.html">
                Make new transactions
              </a>
            </li>
            <li className="nav-item">
              <a className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75" href="Learn.html">
                Learn more about our project!
              </a>
            </li>
            <li className="nav-item">
              <a className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-white hover:opacity-75" href="Learn.html">
                View our white paper!
              </a>
              </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</div>
      <div className="max-w-md w-full">
        <div>
          <img className="mx-auto h-24 w-auto" src={SkynetSVG} alt="Skynet" />
          <h2 className="mt-6 text-center text-4xl sm:text-5xl font-extrabold text-gray-300">
            Algorand Autonomous: MIT Bitcoin Expo 2021
          </h2>
          <p className="mt-2 text-center text-sm leading-5 text-gray-300">
            This is a DOA that is intended act as a hedge fund. This main page allows you to record all of your transactions and view past ones.
          </p>
        </div>

        {authenticated ? (
          <form className="mt-8" onSubmit={handleLogin}>
            <div className="rounded-md shadow-sm">
              <div>
                <textarea
                  rows={3}
                  className="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5"
                  value={transaction}
                  autoFocus={true}
                  onChange={(event) => setTransaction(event.target.value)}
                  placeholder="You did not record a new transaction yet!"
                />
              </div>
            </div>

            <div className="mt-6">
              <button
                type="submit"
                className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-green-600 hover:bg-green-500 focus:outline-none focus:border-green-700 focus:shadow-outline-green active:bg-green-700 transition duration-150 ease-in-out"
                onClick={handleSetTransaction}
                disabled={loading}
              >
                {loading ? "Sending..." : "Save this transaction data"}
              </button>
            </div>

            <div className="mt-2 flex justify-between">
              <button
                onClick={handleReset}
                className="background-transparent text-sm text-green-500 hover:underline outline-none focus:outline-none mr-1 mb-1"
                type="button"
              >
                &larr; go back
              </button>

              {displaySuccess && (
                <span className="text-sm text-green-500 font-bold">
                  Your transaction data has been saved!
                </span>
              )}
            </div>

            {errorMessage && (
              <p className="mt-2 text-sm text-red-500">{errorMessage}</p>
            )}
          </form>
        ) : (
          <form className="mt-8" onSubmit={handleLogin}>
            <input type="hidden" name="remember" value="true" />
            <div className="rounded-md shadow-sm">
            <p className="mt-4 text-center text-2xl sm:text-4xl font-extrabold text-gray-300">
            If this is your first time on the site, please create a secure public key!
            </p>
              <div>
                <input
                  aria-label="Secret Key"
                  name="secret"
                  required
                  className="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5"
                  placeholder="Your secret key."
                  value={secret}
                  onChange={(event) => setSecret(event.target.value)}
                />
              </div>
            </div>

            <div className="mt-6">
              <button
                type="submit"
                className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm leading-5 font-medium rounded-md text-white bg-blue-400 hover:bg-blue-300 focus:outline-none focus:border-blue-700 focus:shadow-outline-blue active:bg-blue-700 transition duration-150 ease-in-out"
              >
                <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                  <svg
                    className="h-5 w-5 text-blue-500 group-hover:text-blue-400 transition ease-in-out duration-150"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fillRule="evenodd"
                      d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                      clipRule="evenodd"
                    />
                  </svg>
                </span>
                Submit
              </button>
            </div>
          </form>
        )}

        <footer className="mt-6 text-center text-sm leading-5 text-gray-300">
          Don't believe us? Look at our code!{" https://github.com/Bhaney44/Cryptots"}
          <a
            className="text-green-500 hover:underline"
            href="https://github.com/Bhaney44/Cryptots"
            target="_blank"
            rel="noopener noreferrer"
          >
            Code Repository
          </a>
          {process.env.REACT_APP_GIT_SHA && (
            <a
              href={`/${process.env.REACT_APP_GIT_SHA}`}
              className="mt-2 block text-xs text-gray-700 hover:underline font-mono"
            >
              {process.env.REACT_APP_GIT_SHA}
            </a>
          )}
        </footer>
      </div>
    </div>
    </div>
  );
}

export default App;
