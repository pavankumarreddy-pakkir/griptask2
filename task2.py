{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing all libraries required in this notebook\n",
    "import pandas as pd\n",
    "import numpy as np  \n",
    "import matplotlib.pyplot as plt  \n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data imported successfully\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1.5</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>9.2</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>5.5</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.3</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2.7</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Hours  Scores\n",
       "0    2.5      21\n",
       "1    5.1      47\n",
       "2    3.2      27\n",
       "3    8.5      75\n",
       "4    3.5      30\n",
       "5    1.5      20\n",
       "6    9.2      88\n",
       "7    5.5      60\n",
       "8    8.3      81\n",
       "9    2.7      25"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reading data from remote link\n",
    "url = \"http://bit.ly/w-data\"\n",
    "s_data = pd.read_csv(url)\n",
    "print(\"Data imported successfully\")\n",
    "\n",
    "s_data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the distribution of scores\n",
    "s_data.plot(x='Hours', y='Scores', style='o')  \n",
    "plt.title('Hours vs Percentage')  \n",
    "plt.xlabel('Hours Studied')  \n",
    "plt.ylabel('Percentage Score')  \n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = s_data.iloc[:, :1].values  \n",
    "y = s_data.iloc[:, -1].values  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split  \n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, \n",
    "                            test_size=0.2, random_state=0) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training complete.\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression  \n",
    "regressor = LinearRegression()  \n",
    "regressor.fit(X_train, y_train) \n",
    "\n",
    "print(\"Training complete.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the regression line\n",
    "line = regressor.coef_*X+regressor.intercept_\n",
    "\n",
    "# Plotting for the test data\n",
    "plt.scatter(X, y)\n",
    "plt.plot(X, line);\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.5]\n",
      " [3.2]\n",
      " [7.4]\n",
      " [2.5]\n",
      " [5.9]]\n"
     ]
    }
   ],
   "source": [
    "print(X_test) # Testing data - In Hours\n",
    "y_pred = regressor.predict(X_test) # Predicting the scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual</th>\n",
       "      <th>Predicted</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>16.884145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27</td>\n",
       "      <td>33.732261</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69</td>\n",
       "      <td>75.357018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30</td>\n",
       "      <td>26.794801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>60.491033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Actual  Predicted\n",
       "0      20  16.884145\n",
       "1      27  33.732261\n",
       "2      69  75.357018\n",
       "3      30  26.794801\n",
       "4      62  60.491033"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Comparing Actual vs Predicted\n",
    "df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  \n",
    "df "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Expected 2D array, got scalar array instead:\narray=9.\nReshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-0259ceea3b08>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# You can also test with your own data\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mhours\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m9\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mown_pred\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mregressor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhours\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"No of Hours = {}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhours\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Predicted Score = {}\"\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mown_pred\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_base.py\u001b[0m in \u001b[0;36mpredict\u001b[1;34m(self, X)\u001b[0m\n\u001b[0;32m    234\u001b[0m             \u001b[0mReturns\u001b[0m \u001b[0mpredicted\u001b[0m \u001b[0mvalues\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    235\u001b[0m         \"\"\"\n\u001b[1;32m--> 236\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_decision_function\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    237\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    238\u001b[0m     \u001b[0m_preprocess_data\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstaticmethod\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_preprocess_data\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\linear_model\\_base.py\u001b[0m in \u001b[0;36m_decision_function\u001b[1;34m(self, X)\u001b[0m\n\u001b[0;32m    216\u001b[0m         \u001b[0mcheck_is_fitted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    217\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 218\u001b[1;33m         \u001b[0mX\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcheck_array\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maccept_sparse\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'csr'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'csc'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'coo'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    219\u001b[0m         return safe_sparse_dot(X, self.coef_.T,\n\u001b[0;32m    220\u001b[0m                                dense_output=True) + self.intercept_\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\u001b[0m in \u001b[0;36minner_f\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     71\u001b[0m                           FutureWarning)\n\u001b[0;32m     72\u001b[0m         \u001b[0mkwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mk\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mzip\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msig\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 73\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     74\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0minner_f\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     75\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\u001b[0m in \u001b[0;36mcheck_array\u001b[1;34m(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator)\u001b[0m\n\u001b[0;32m    611\u001b[0m             \u001b[1;31m# If input is scalar raise error\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    612\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0marray\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mndim\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 613\u001b[1;33m                 raise ValueError(\n\u001b[0m\u001b[0;32m    614\u001b[0m                     \u001b[1;34m\"Expected 2D array, got scalar array instead:\\narray={}.\\n\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    615\u001b[0m                     \u001b[1;34m\"Reshape your data either using array.reshape(-1, 1) if \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Expected 2D array, got scalar array instead:\narray=9.\nReshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample."
     ]
    }
   ],
   "source": [
    "# You can also test with your own data\n",
    "#hours = 9\n",
    "#own_pred = regressor.predict(hours)\n",
    "#print(\"No of Hours = {}\".format(hours))\n",
    "#print(\"Predicted Score = {}\".format(own_pred[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Absolute Error: 4.183859899002982\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics  \n",
    "print('Mean Absolute Error:', \n",
    "      metrics.mean_absolute_error(y_test, y_pred)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
