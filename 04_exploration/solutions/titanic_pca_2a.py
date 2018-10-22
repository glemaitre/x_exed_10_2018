pca_pipeline = make_pipeline(preprocessor, PCA(n_components=16))
pca_pipeline.fit(data.dropna())
sns.pairplot(pd.DataFrame(pca_pipeline.transform(data.dropna())))
